#!/bin/bash

set -e

# software requirements:  
#   awk, jq, pg_dump, psql
#   cloudfoundry cli (cf)
#   post
# prerequisite:
#   empty postgres database named invest-dev
#   cf ssh   to invest-staging needs to work
#
# The DB dumps may contain references to postgis and will need those
# packages, on ubuntu they are installed with:
#
# sudo apt install postgis postgresql-10-postgis-2.4 -y 
#
usage() {
    >&2 echo 'Usage: $ clone-db.sh cf-app postgres-db-url'
    >&2 echo ''
    >&2 echo 'Example:'
    >&2 echo '$ clone-db.sh invest-staging postgres://username:password@localhost:54321/invest-dev'
    >&2 echo ''
    >&2 echo 'Environment variables'
    >&2 echo 'DATABASE_URL is used it it is not set'    
    exit 0
}

wait_for_postgres() {
    WAIT_CMD="pg_isready --dbname=$1"
    DELAYS="0.1 0.1 0.1 0.1  2 1 1 2 2 5 8 12 15"
    DELAY=1
    DOTS="..."
    set +e
    for DELAY in $DELAYS; do
        if $WAIT_CMD > /dev/null; then
           >&2 echo -ne "\033[2KConnect to postgres [OK]\n"
           return
        fi
        >&2 echo -ne "Connect to postgres $DOTS\r"
        sleep $DELAY
        DOTS="$DOTS."
    done
    >&2 echo "Couldn't connect to postgres, quitting."
    exit 1
}


### Start
#
if [[ $# -eq 0 ]] ; then
    usage
fi

if [[ $# -gt 0 ]] ; then
    CFAPP=$1
    if [ ! -z $2 ] ; then
        DATABASE_URL=$2
    fi
    if [ -z ${DATABASE_URL} ] ; then
        echo >&2 'Specify a database or set DATABASE_URL'
        exit 1
    fi
fi

### database backup
#

DUMP_SQL=${CFAPP}.sql
unset DB_USER DB_NAME

# Get database settings from cloudfoundry

# Use awk to grab the json between the strings 'System-Provided and User-Provided
# Pass it to jq to grab the database connection details to env vars named like
# DB_(json key) 

. <(cf env ${CFAPP} | \
  awk '/System-Provided:/{flag=1;next}/User-Provided:/{flag=0}flag' | \
  jq -r '.VCAP_SERVICES?.postgres[0].credentials? | select(.!=null) | to_entries[] | "\("DB_"+.key | ascii_upcase)=\(.value)"')

TMPDIR=/tmp/invest-data/${CFAPP}
mkdir -p ${TMPDIR}

# These variables are available
# DB_HOST
# DB_JDBCURI
# DB_NAME
# DB_PASSWORD
# DB_PORT
# DB_URI
# DB_USERNAME

# Build URI on the port we will forward
LOCAL_DB_PORT=15432
LOCAL_DB_URI=postgresql://$DB_USERNAME:$DB_PASSWORD@localhost:$LOCAL_DB_PORT/$DB_NAME

close_ssh () {
    echo >&2 "Close SSH PID: $SSH_PID"
    kill $SSH_PID
    exit $ARG
} 
trap close_ssh EXIT

# Connect to cloudfoundry and setup tunnel so we can dump the db
cf ssh ${CFAPP} -N -L ${LOCAL_DB_PORT}:${DB_HOST}:5432 & SSH_PID=$!
echo  >&2 "SSH PID: $SSH_PID"

wait_for_postgres ${LOCAL_DB_URI}

set +e
echo  >&2 'Dump DB: ' ${TMPDIR}/${DUMP_SQL}
DUMP_CMD="pg_dump --clean --no-owner --no-privileges --dbname ${LOCAL_DB_URI}"
$DUMP_CMD > ${TMPDIR}/${DUMP_SQL}

### Database restore
#
echo >&2 "Restore DB"
psql --dbname ${DATABASE_URL} -f ${TMPDIR}/${DUMP_SQL} > /dev/null


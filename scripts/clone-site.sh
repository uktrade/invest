#!/bin/bash

set -e
# You *really* want to use this via clone-site.sh so that the database matches,
# but it's up to you.
usage() {
    >&2 echo 'Usage: $ clone-site.sh cf-app postgres-db-url'
    >&2 echo ''
    >&2 echo 'Example:'
    >&2 echo '$ clone-site.sh invest-staging postgres://username:password@localhost:54321/invest-dev'
    exit 0
}


### Start
#
if [[ $# -lt 1 ]] ; then
    usage
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CFAPP=$1

$DIR/clone-db.sh $1 $2
$DIR/clone-bucket.sh $1


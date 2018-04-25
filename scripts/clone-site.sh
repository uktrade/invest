#!/bin/bash

set -e
# You *really* want to use this via clone-site.sh so that the database matches,
# but it's up to you.
usage() {
    >&2 echo 'Usage: $ clone-site.sh cf-app postgres-db-url [media directory]'
    >&2 echo ''
    >&2 echo 'Example:'
    >&2 echo '$ clone-site.sh invest-staging postgres://username:password@localhost:54321/invest-dev'
    >&2 echo ''
    >&2 echo "Pass in media directory to use a folder other than the default for clone-bucket.sh"
    >&2 echo "media directory must be a folder that already exists."
    exit 0
}


### Start
#
if [[ $# -lt 1 ]] ; then
    usage
fi

if [[ $# -eq 2 ]] && [ -d $2 ] ; then
    MEDIA_DIR=$2
elif [[ $# -eq 3 ]] && [ -d $3 ] ; then
    MEDIA_DIR=$2
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CFAPP=$1

echo $DIR/clone-bucket.sh $1 $MEDIA_DIR

$DIR/clone-bucket.sh $1 $MEDIA_DIR
# $DIR/clone-db.sh $1 $2


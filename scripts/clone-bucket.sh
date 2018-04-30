#!/bin/bash

PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/../" && pwd )"
DEFAULT_MEDIA_DIR=../config/media

# You *really* want to use this via clone-site.sh so that the database matches,
# but it's up to you.
set -e
usage() {
    >&2 echo 'Usage: $ clone-bucket.sh cf-app [media directory]'
    >&2 echo ''
    >&2 echo 'Example:'
    >&2 echo '$ clone-bucket.sh invest-staging'
    >&2 echo ''
    >&2 echo "Pass in media directory to use a folder other than the default at $DEFAULT_MEDIA_DIR"
    exit 0
}


### Start
#
if [[ $# -eq 0 ]] ; then
    usage
fi

if [[ $# -gt 1 ]] ; then
    MEDIA_DIR=$2
else
    MEDIA_DIR=$PROJECT_DIR/config/media
fi

CFAPP=$1

# Yoink the credentials from the cf-app
export $(cf env ${CFAPP} | \
  awk '/User-Provided:/{flag=1;next}/^$/{flag=0}flag' | \
  grep -e 'AWS_ACCESS_KEY_ID' -e 'AWS_SECRET_ACCESS_KEY' -e 'AWS_STORAGE_BUCKET_NAME' | sed "s/\: /\=/g")

# Sync the files ...
2>&1 echo "Clone media to: $MEDIA_DIR"
SYNC_CMD="aws s3 sync s3://$AWS_STORAGE_BUCKET_NAME $MEDIA_DIR"
$SYNC_CMD
2>&1 echo "Done."


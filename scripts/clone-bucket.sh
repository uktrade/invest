#!/bin/bash

# You *really* want to use this via clone-site.sh so that the database matches,
# but it's up to you.
set -e
usage() {
    >&2 echo 'Usage: $ clone-bucket.sh cf-app'
    >&2 echo ''
    >&2 echo 'Example:'
    >&2 echo '$ clone-bucket.sh invest-staging'
    exit 0
}


### Start
#
if [[ $# -eq 0 ]] ; then
    usage
fi

PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/../" && pwd )"

CFAPP=$1
MEDIA_DIR=$PROJECT_DIR/config/media

# Yoink the credentials from the cf-app
export $(cf env ${CFAPP} | \
  awk '/User-Provided:/{flag=1;next}/^$/{flag=0}flag' | \
  grep -e 'AWS_ACCESS_KEY_ID' -e 'AWS_SECRET_ACCESS_KEY' -e 'AWS_STORAGE_BUCKET_NAME' | sed "s/\: /\=/g")

# Sync the files ...
echo "Cloning media"
SYNC_CMD="aws s3 sync s3://$AWS_STORAGE_BUCKET_NAME $MEDIA_DIR"
$SYNC_CMD

#!/bin/bash
DIR="$( dirname "$0" )"
EXEC="$( "${DIR}"/openbydomain.py "$@" )"
STATUS=$?
echo "$EXEC" $STATUS

if [ $STATUS -eq 0 ] && [ "$EXEC" ]; then
 "$EXEC" "$@" # &
fi

exit $STATUS

#! /bin/bash
# This file is a resource lock, as multi-worker use one static resource.
# The resource should be used by one worker at one time.
# Ctrl+C is handled, when the key pressed, resource released.

FILE=/tmp/rlock

function create_file() {
    [ -f $FILE ] || touch $FILE
}

function lock() {
    if [ "x"`cat $FILE` = "x" ]; then
        echo "lock" > $FILE
    else
        echo "resource locked!!"
        exit 1
    fi
}

function unlock() {
    echo "" > $FILE
}

trap unlock 2

create_file
lock
# Sleep should changed to the program, which need lock resource.
sleep 3
unlock

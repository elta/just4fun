#! /bin/bash

if [ ! -d "/Volumes/mnt" ]; then
    sudo mkdir -pv /Volumes/mnt
fi

sudo mount -t exfat,local,nodev,nosuid,noowners /dev/disk3s1 /Volumes/mnt/


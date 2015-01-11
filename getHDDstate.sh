#!/bin/bash

drive="/dev/$1"

if sudo /usr/bin/hdparm -C "$drive"| grep -q standby
then
    echo -n "$1 Ú"
    exit 0
else
    echo -n "$1 Û"
    exit 1
fi

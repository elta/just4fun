#! /bin/bash

IPS=$(/sbin/ifconfig -a | grep -i inet | grep -iv inet6 | awk {'print $2'} | sed -ne 's/addr\://p')

echo $IPS

for IP in $IPS; do
    echo "Current IP is ${IP}"
done

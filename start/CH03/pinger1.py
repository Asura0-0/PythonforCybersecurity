#!/usr/bin/env python3
# First example of pinging from Python
# By Aahan 1/14/24

import os

#Assign IP address to a variable
ip_address = "127.0.0.1"

#build our ping cmd
ping_cmd = "ping -n 1 -w 1 {0} > NUL 2>&1".format(ip_address)

# execute the ping cmd
exit_code = os.system(ping_cmd)

# print results
print(exit_code)

#!/usr/bin/env python3
# Second example of pinging from Python
# By Aahan 1/14/24

import os
import platform

#Assign IP address to a variable
ip_address = "127.0.0.1"
#find our os
current_os = platform.system().lower()
if current_os == "windows":
    #build our ping cmd Windows
    ping_cmd = "ping -n 1 -w 1000 {0} > NUL 2>&1".format(ip_address)
else:
    #build our ping cmd Linux
    ping_cmd = "ping -n 1 -w 1 {0} > /dev/null 2>&1".format(ip_address)


# execute the ping cmd
exit_code = os.system(ping_cmd)
# print results
print(exit_code)

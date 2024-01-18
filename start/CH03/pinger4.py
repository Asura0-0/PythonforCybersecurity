#!/usr/bin/env python3
# Third example of pinging from Python
# By Aahan 1/18/24

import os
import platform

def ping_address(ip_address):
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
    if exit_code == 0:
        return True
    return False

#Assign IP address to a variable
ip_prefix = "192.168.1."
#for loop 1-255
for octet in range (255):
    # setup IP address
    ip_address = ip_prefix + str(octet + 1)
    
    #call function
    result = ping_address(ip_address)

    # print results
    if result == True:
        print("{0} is online".format(ip_address))

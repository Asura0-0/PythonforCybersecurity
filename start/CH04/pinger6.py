#!/usr/bin/env python3
# Sixth example of pinging from Python
# Writing log messages to a file
# By Aahan 4/21/24

import os
import platform
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))

def write_log(message):
    # Get current time/date
    now = str(datetime.now()) + '\t'
    message = now +  str(message) + "\n"
    # Open a log file for appending
    f = open(dir_path + "/pinger.log", "a")
    # Write my message wit date/time
    f.write(message)
    # Close file
    f.close()

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

# Open file for reading
f = open(dir_path+ "/ips.txt", "r")
# Reading file
ip_addresses = f.readlines()
# Close file
f.close
# Loop through results
for ip_address in ip_addresses:
    # Cleam up ip address
    ip_address = ip_address.strip()
    # call function
    result = ping_address(ip_address)

    # print results
    if result == True:
        print("{0} is online".format(ip_address))
        write_log("{0} is online".format(ip_address))
    else:
        write_log("{0} \n is OFFLINE".format(ip_address))

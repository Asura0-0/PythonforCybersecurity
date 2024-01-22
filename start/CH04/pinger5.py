# By #!/usr/bin/env python3
# Fifth example of pinging from Python
# Reading IPs from a file
# By Aahan 1/32/24

import os
import platform

dir_path = os.path.dirname(os.path.realpath(__file__))

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

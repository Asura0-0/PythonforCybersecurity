#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Aahan 2/13/24

import os
# prompt for file
log_file = input("which file do you want to scan? ")
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path+ "/"+ log_file, "r")

# Read file line by line
while True:
    line = f.readline()
    if not line:
        break
    # Loop to look for 404
    # if "404" in line:
    #     print(line.strip())
    if "162.239.205.0" in line:
        if "404" in line:
            print(line.strip())

# Close file
f.close()

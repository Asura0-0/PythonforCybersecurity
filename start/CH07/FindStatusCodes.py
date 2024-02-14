#!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By #!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Aahan 2/13/24

import os
import re
# prompt for file
log_file = input("which file do you want to scan? ")
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path+ "/"+ log_file, "r")
<<<<<<< HEAD
log_lines = f.readlines()
f.close()

# setup regex pattern and dictionary
reg_pat = r"\s(\d{3})\s"
result_dictionary = {}

# Find match in file an dstore in dictionary
for line in log_lines:
    # Search for pattern, i found, store it
    m = re.search(reg_pat, line)
    if m:
        status_code = m.group()
        # Store status in dictionary
        if status_code in result_dictionary.keys():
            result_dictionary[status_code] += 1
        else:
            result_dictionary[status_code] = 1

print(result_dictionary)
=======

# setup regex pattern and dictionary


# Find match in file an dstore in dictionary

        # Search for pattern, i found, store it



>>>>>>> b07fbafbe68b0d3bc4d9181d553dc41731796294
# sort and print most frequent result
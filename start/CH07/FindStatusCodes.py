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

# setup regex pattern and dictionary


# Find match in file an dstore in dictionary

        # Search for pattern, i found, store it



# sort and print most frequent result
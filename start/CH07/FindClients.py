# By #!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By Aahan

#Import Python modules
import os
import re
# prompt for file
log_file = input("which file do you want to scan? ")
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path+ "/"+ log_file, "r")
log_lines = f.readlines()
f.close()

# Setup regex pattern and empty dictionary
regex_pat = r"^([0-9]{1,3}\.){3}[0-9]{1,3}"
result_dictionary = {}

# Find match and store in dictionary
for line in log_lines:
    # Search for pattern, and if found move forward
    m = re.search(regex_pat, line)
    if m:
        status_code = m.group()
        # store status in dictionary
        if status_code in result_dictionary.keys():
            result_dictionary[status_code] += 1
        else:
            result_dictionary[status_code] = 1

# print(result_dictionary)
# for key in result_dictionary.keys():
#     print("{0} - {1}".format(key, result_dictionary[key]))

# Sort and print most frequent rsult
for w in sorted(result_dictionary, key=result_dictionary.get, reverse=False):
    print(w, result_dictionary[w])

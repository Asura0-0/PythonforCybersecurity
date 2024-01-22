#!/usr/bin/env python3
# Sample script that writes to a file
# By Aahan 1/21/24

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Open file for writing
f = open(dir_path+ "/testfile.txt", "r")

# Read file and print
contents = f.read()
print(contents)

# close file
f.close()
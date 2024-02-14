#!/usr/bin/env python3
# Script that hashes a password
# By 

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path+ "/shadow.txt", "r")
pw = f.readlines()
passwords = pw[11:]
f.close

print(passwords)
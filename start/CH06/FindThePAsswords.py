#!/usr/bin/env python3
# Script that hashes a password with provided salt
# By Aahan 2/7/24

import crypt
import os

# Functions to test password
def test_password(algorithm_salt, hashed_password, password_guess):
    # Use salt to has guess
    hashed_guess = crypt.crypt(password_guess, algorithm_salt)
    #compare salt guess against hashed password
    if hashed_guess == hashed_password:
        return True
    return False

# Get list of passwords to use
with open("/home/aahan/PythonforCybersecurity/start/CH06/top10million.txt", "r") as f:
    passwords = f.readlines()

# Get the hashed password to crack
with open("/home/aahan/PythonforCybersecurity/start/CH06/shadow", "r") as f:
    pw = f.readlines()
    hashed = pw[11:]

for password, hash in zip(passwords, hashed):
    password = password.strip()
    hash = hash.strip()
    algorithm_salt = hash[12:27]
    hashed_password = hash[29:115]
        
    result = test_password(algorithm_salt, hashed_password, password)
    if result:
        print("MAtch found: {0}".format(password))
        break


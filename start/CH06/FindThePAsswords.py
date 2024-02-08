#!/usr/bin/env python3
# Script that hashes a password with provided salt
# By Aahan 2/7/24

import crypt
import os

# Functions to test password
def test_password(alorithm_salt, hashed_password, password_guess):
    # Use salt to has guess
    hashed_guess = crypt.crypt(password_guess, alorithm_salt)
    #compare salt guess against hashed password
    if hashed_guess == hashed_password:
        return True
    return False

# Load dictionary file
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path+ "/shadow.txt", "r")
pw = f.readlines()
passwords = pw[11:]
f.close

# Promt user for Algorithm/salt
algorithm_salt = input("What is the algorithm and salt? ")

# Promt user for salt has
hashed_password = input("what is the full hashed password? ")

# Loop through each password
for password in passwords:
    password = password.strip()
    result = test_password(algorithm_salt, hashed_password, password)
    if result:
        print("MAtch found: {0}".format(password))
        break

for password in passwords:
    password = password.strip()
    result = test_password(algorithm_salt, hashed_password, password)
    if result:
        print("MAtch found: {0}".format(password))
        break




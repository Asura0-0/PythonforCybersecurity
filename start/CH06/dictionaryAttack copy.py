<<<<<<< HEAD
#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Aahan 2/7

# Import MOdules
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

# Get list of passwords to use
with open("/home/aahan/PythonforCybersecurity/start/CH06/top10million.txt", "r") as f:
    passwords = f.readlines()
# Promt user for Algorithm/salt
algorithm_salt = input("WHat is the algorithm and salt? ")

# Promt user for salt has
hashed_password = input("what is the full hashed password? ")

# Loop through each password
for password in passwords:
    password = password.strip()
    result = test_password(algorithm_salt, hashed_password, password)
    if result:
        print("MAtch found: {0}".format(password))
=======
#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Aahan 2/7

# Import MOdules
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

# Get list of passwords to use
with open("/home/aahan/PythonforCybersecurity/start/CH06/top10million.txt", "r") as f:
    passwords = f.readlines()
# Promt user for Algorithm/salt
algorithm_salt = input("WHat is the algorithm and salt? ")

# Promt user for salt has
hashed_password = input("what is the full hashed password? ")

# Loop through each password
for password in passwords:
    password = password.strip()
    result = test_password(algorithm_salt, hashed_password, password)
    if result:
        print("MAtch found: {0}".format(password))
>>>>>>> b07fbafbe68b0d3bc4d9181d553dc41731796294
        break
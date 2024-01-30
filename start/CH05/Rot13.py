#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Aahan 1/29/24

# Ask for msg
print("What is your message? ")
source_message = input()

# change msg to lowercase
source_message = source_message.lower()
final_message = ""

# Loop thru each letter in msg
for letter in source_message:
    # Conver letter to number
    ascii_number = ord(letter)
    # check if letter is a-z
    if ascii_number >= 97 and ascii_number <= 122:
        # Add 13 to numebr
        ascii_number += 13
        # Check if still a letter, if not subtact 26
        if ascii_number > 122:
            ascii_number -= 26
    final_message = final_message + chr(ascii_number)    

# Print out message
print(final_message)


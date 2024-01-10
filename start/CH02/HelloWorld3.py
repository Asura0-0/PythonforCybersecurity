#!/usr/bin/env python3
# A simple "Hello World" script in python with Inputs
# Created Aahan - 1/10/24

# Suggestion, build out 1 line at a time
# Once multiple print statemetns exist, put a breakpoint at first print line
# Then walk through as an example of "debugging"

# Ask user for name
user_name = input("What is your name? ")

#print hello and their name
print("Hello {0}".format(user_name))
print(f"Hello {user_name}")
print("Hello " + user_name)
print("Hello", user_name)
message = "hello " + user_name
print(message)
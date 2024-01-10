#!/usr/bin/env python3
# A simple "Hello World" script in python with Inputs
# Created Aahan - 1/10/24

# Suggestion, build out 1 line at a time
# Once multiple print statemetns exist, put a breakpoint at first print line
# Then walk through as an example of "debugging"

# Ask user for name
user_name = input("What is your name? ")

#print hello and their name
print("Hello", user_name, "\nToday is going to be a great day!")

#Daring part - user's Age
user_age = input("What is your age?")
user_age =int(user_age)
future_age = user_age+2
print(f"In 2 years, you will be {future_age} years old")


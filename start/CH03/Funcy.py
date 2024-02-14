#!/usr/bin/env python3
# example workign with Functions
#By Aahan 1/18/24

#This is my function
def print_me( my_message):
    print(my_message)
    return "it worked"

def say_hello(num_times):
    for x in range(num_times):
        print("Hello World")

#Calling the functio
print_me("This is a function")
result = print_me("this is another function with a return value")
print(result)

say_hello(3)
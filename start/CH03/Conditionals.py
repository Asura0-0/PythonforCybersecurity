#!/usr/bin/env python3
# example workign with conditionals
#By Aahan 1/14/24

def send_message():
    for i in range(10):
        print("Yes it is")

#Ask how day is
day = input("Is today a good day? \n (y/n) ")

#If statment for y
if day == "y":
    send_message()
else:
    print("Womp womp")


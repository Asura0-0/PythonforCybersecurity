#!/usr/bin/env python3
# example workign with conditionals
#By Aahan 1/14/24

#Ask how day is
day = input("Is today a good day? \n (y/n) ")

#If statment for y
if day == "y":
    for i in range(10):
        print("Yes it is")
else:
    print("Womp womp")
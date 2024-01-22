#
#
# By Aahan 1/22/24

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path+ "/hackme.txt", "w")
f.close()

name = input("What is your name? ")
color = input("what is your favorite color? ")
pet_name = input("What is your first pet's name? ")
maiden = input("What is your mother's maiden name? ")
school = input("What elementary school did you attend? ")      

with open(dir_path+ "/hackme.txt", "w") as f:
    f.write("Name: {0}\n".format(name))
    f.write("Color: {0}\n".format(color))
    f.write("Pet Name: {0}\n".format(pet_name))
    f.write("Mother's Maiden Name: {0}\n".format(maiden))
    f.write("Elementary School: {0}\n".format(school))
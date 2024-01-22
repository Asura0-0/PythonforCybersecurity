#
#
# By Aahan 1/22/24

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

print("Here is someone to hack - information")

with open(dir_path+ "/hackme.txt", "r") as f:
    info = f.read()
print(info)
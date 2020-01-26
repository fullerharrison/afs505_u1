# From terminal import arguments
from sys import argv
#Read the WYSS section for how to run this
# the name of the file or script is the first arguement
# then input by user is the 2nd 3rd and 4th arguements
script, first, second, third  = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

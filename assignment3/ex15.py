# from the terminal retrieve arguents argv
from sys import argv
# the script name and the filename are used to satisfy the script
script, filename = argv
# python opens the file inputed by user
txt = open(filename)
# prints this statement including filename
print(f"Here's your file {filename}:")
# prints or reads the contents of the fil on to terminal
print(txt.read())
# Retrieves input from the user and stores in a variable
print("Type the filename again:")
file_again = input("> ")

# prompts a variable to open a file inputed by the user
txt_again = open(file_again)

print(txt_again.read())

from sys import argv

script, filename = argv

# orints the commands of action for the file of interest or inputed
print(f"We're going to erase {filename}.")
print("If toy don't want that, hit CTRL-C (^C).")
print("If you dont't want that, hit RETURn.")

#Waits for user input
input("?")
# Opens file to be examined and prepares for edits
print("Opening the file ...")
target = open(filename, 'w')
# OPens file of interest for truncation, truncating is not neccessary
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
# Waits for user input
Line1 = input("Line 1: ")
Line2 = input("Line 2: ")
Line3 = input("Line 3: ")

print("I'm going to write these to file.")
#writes in existing file new lines provided by user
target.write(Line1)
target.write("\n")
target.write(Line2)
target.write("\n")
target.write(Line3)
target.write("\n")
# Close the work done.
print("And finally, we close it.")
target.close()

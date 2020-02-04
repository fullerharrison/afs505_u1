from sys import argv
# import script and arguement from terminal
script, input_file = argv

# make a function that print the out put of reading a file.
def print_all(f):
    print(f.read())

# reverse the text of outputed file and move to position 0 or firsdt position
# Looks at bytes not rows
def rewind(f):
    f.seek(0)
# function for printting a line
def print_a_line(line_count, f):
    print(line_count, f.readline())
# variable that prints individual lines
current_file = open(input_file)

print("First let's print the whole file:\n")
# prints entire file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# Calls the rewind funcction and original file
rewind(current_file)

print("Let's print three lines:")
# prints first line
current_line = 1
print_a_line(current_line, current_file)
# prints second line
current_line += 1
print_a_line(current_line, current_file)
# prints third line
current_line += 1
print_a_line(current_line, current_file)

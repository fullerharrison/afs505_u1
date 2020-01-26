from sys import argv
from os.path import exists
# importing packages and sub packages
# echo "This is a test file." > test.txt
# cat test.txt
# What does this do?
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
# Not sure... encapsulating read(from_file.open()) Does
# Not work
in_file = from_file.open()
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
# Writes contents of indata to to_file
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
# Closes all files
out_file.close()
in_file.close()

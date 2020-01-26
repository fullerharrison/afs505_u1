from sys import argv
from os.path import exists

from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

 # we could do these two on one line, how?
 # open a file handle and then reads the file into a string
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
# The w will creat if it doesn't exists
# or clear it out
out_file = open(to_file, 'w')
out_file.write()

print("Alright, all done.")

out_file.close()
in_file.close()

import sys
script, input_encoding, error = sys.argv
# import package that seeks 3 arguements from terminal

def main(language_file, encoding, errors):
    line = language_file.readline()
# conditional statement that calls print_line function to variable print_line
# depending if their is a file to readline
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
# prints line of text one line at a time
# prints the encoding of the language and the associated raw_bytes
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)
#opens file prompted in terminal
languages = open("languages.txt", encoding = "utf-8")
#calls to main function for reading file
main(languages, input_encoding, error)

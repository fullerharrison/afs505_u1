# variable that contains 4 format arguements
formatter = "{} {} {} {}"

# prints numbers in for the 4 format arguements
print(formatter.format(1, 2, 3, 4))

# prints words in the 4 format arguements
print(formatter.format("one", "two", "three", "four"))

# prints boolean for the 4 format arguements
print(formatter.format(True, False, False, True))

# prints 4 {} for each arguement
print(formatter.format(formatter, formatter, formatter, formatter))

# prints the only the first 4 formatted objects
print(formatter.format(
"Roses are red,",
"violets are blue,",
"I like Python,",
"how about you?", "Yeeeeees"
))

def main():
    from sys import argv
    script, filename = argv
    filehand = open(filename)
# create our data frame
    data = ["Biosample", "Experiment", "Run", "Time", "Organism", "Tissue",
    "Variety", "Abbrv", "Subspecies", "IRGC_Num"]
    my_list = []
    headers = text.readline().split("\t")
    while headers:
        for i in range(len(headers)):

            if i == data:
                data = data[i]
                pass









    line_count = 0
    # count all words in filehand
    word_count = 0
    # count all characters in filehand
    character_count = 0
    line = filehand.readline()
    while line:
        # While true each iteration represents a line
        line_count +=1
        # While true each iteration counts the length
        # of line = the total number of characters
        character_count += len(line)
        # While true each iteration will split the string by empty
        # characters and make a new list. Then count the number of objects
        # in that new list
        word_count += len(line.split())
        # Indicating a new line for while loop
        line = filehand.readline()

    print(line_count, word_count, character_count, f"file: {filename}")
if _name_ == "_main_":
    main()

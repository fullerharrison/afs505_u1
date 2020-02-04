import csv
# I want to make a more technical approach to this 'story'

# function for opening and picking Raman shift data
def data_extract():
    #gets user input for data
    master = open(input("Enter Raman data file name: "), newline = '')
# Empty list for data
    raman_data = []
    for row in master:
        for col in master:
            if master[row] == "Raman Shift":
                print("nice")
                #print(master[row])
                raman_data = master[row]
                pass

            else:
                pass
                print("pass")



    pass
    # Passes data into manipulation
    #data_manipulation(data_file)


def data_manipulation():
    raman_data = []
    if colname() == "Raman Shift":
        raman_data = raman.append()
        pass


def directory_scan():
    for filename in os.listdir(directory):
        if filename.endswith(".csv") or filename.endswith(".py"):
             # print(os.path.join(directory, filename))
            pass
        else:
            pass
data_extract()

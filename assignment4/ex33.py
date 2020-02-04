# fuction that takes two inputa and passes them into list biuilding
def main(x,y):
    # place holder
    i = 0
    # empty List
    numbers = []
    # bollean condtional statemnt
    while i < int(x):
        print(f"At the top i is {i}")
        numbers.append(i)
        # increment determent for loop
        i += int(y)
        #print(x)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

        print("The numbers: ")

        for num in numbers:
            print(num)
# call to function using 2 input variables
#main(input(), input())

def main1(a, b):
    i = 0
    numbers = []
    for i in range(0,int(a), int(b)):
        print(f"At the top i is {i}")
        numbers.append(i)
        i += int(b)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

        print("The numbers: ")

        for num in numbers:
            print(num)
main(input(), input())

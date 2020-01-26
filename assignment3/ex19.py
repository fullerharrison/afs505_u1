# Creates a function named cheese_and_crackers
#passes 2 variables or arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
# passes numbers as arguements
print("We can give the function numbers directly:")
cheese_and_crackers(20, 30)

#Passes numbers as variables to be manipulated
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# Passes variables in function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Prints new arguements
print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)
# Combines variables and passes in function
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

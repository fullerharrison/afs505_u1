people = 30
cars = 40
trucks = 15
# If states the first logical statement
# elif adresses the next logical statement
# else is the ultimatum if logical expressions are not satisfied

# Tests if statement cars < people and trucks < people is T
if cars < people and trucks < people:
    print("We should take the cars.")
# Checks if statement is T
elif cars == people:
    print("We should not take the cars.")
else: #prints ultimatum if previouis statements are false
    print("We can't decide.")
# evaluates the number of trucks
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars: #evaluates the nunber of trucks to cars
    print("Maybe we could take the trucks.")
else:# if decisions return false print this statement
    print('We still can\'t decide')
# Evaluates the number of trucks to people for decision
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# list of integers
the_count = [1,2,3,4,5]
# list of strings
fruits = ['apples', 'oranges', 'pears', 'apricots']
# List of strings and numbers
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list.
# 5 integers so loops 5 times
for number in the_count:
    print(f"This is a count {number}")

# Same as above
# 4 fruits in list fruits so loops 4 times
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# Also we can go through mixed lists too
# prints contents of list with length 'change'
for i in change:
    print(f"I got {i}")

# WE can also builf lists, first start with an empty one
# empty list
elements = []

#Then uise the range function to do 0 to 5 counts
# range(start, stop[ ,steps or increments])
for i in range(0,5):
    print(f"Adding {i} to the list.")
    # Append is a function that lists understands
    elements.append(i)

# Now we can print them out too

for i in elements:
    print(f"Element was: {i}")

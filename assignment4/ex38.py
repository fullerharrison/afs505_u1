# list of on single string
ten_things = "Apples Oranges Crows Telephone Light Sugar"
# dialogue
print("Wait there are not 10 things in that list. Let's fix that.")
# splits the single string by ' ' and assigns new variable
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn",
                "Banana", "Girl", "Boy"]
# condition that will end the loop at 10 items in the list
while len(stuff) != 10:
    # Removes from the end of list more_stuff
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} item s now.")

print("There we go: ", stuff)

print("Let's do some things with my stuff")
# Looks at the 2nd item
print(stuff[1])
# calls the last item
print(stuff[-1])
# print the last item of stuff
print(stuff.pop())
# Joins the list of stuff  with ' '
print(' '.join(stuff))
# joins the 3rd and 4th elements with #
print('#'.join(stuff[3:5]))

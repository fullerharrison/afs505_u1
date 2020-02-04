# Begins the game
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")
# asks for user input
door = input("> ")
# conditional statement based on user input
if door  == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
# promps 'bear' input
    bear = input("> ")
# conditional moment for bear decision
    if bear == "1":
        print("The bear eats your face off. Good job!")

    elif bear == "2":
        print("Stay or run?")
        action == input('> ')
        if action == "Run":
            print("You got away")
        else:
        print("The bear eats your legs off. Good job!")

    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
# condition of the scecond statement
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
# promps for second decision
    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")

    else:
        print("The insanity rots your eyes into a pool of much.")
        print("Good job!")
# if 1 or 2 are not selected
else:
    print("You stumble around and fall on a knife and die. Good job!")

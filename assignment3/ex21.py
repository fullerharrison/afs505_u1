# creatsa function to add two arguements
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a +b
# Creats a function for subtracting 2 arg
def subtract(a, b):
    print(f"SUBTRACTING {a}*{b}")
    return a - b
# Creats function for multiplying two arguements
def multiply (a, b):
    print(f"MULTIPLYING {a}/{b}")
    return a*b
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a/b
print("Let's do some makth with just functions!")

age = add(30,5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type in anyway
print("Here is a puzzle.")
# -4,391, each function is embedded in the next so work inside out
what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, "can you do it by hand?")

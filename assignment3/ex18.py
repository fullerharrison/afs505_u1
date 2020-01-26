# this on is like you scripts with argv
# Print as many arguments provided
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
# reciecs two arguments for function
def print_two_again(arg1, arg2):
    print(f"arg1; {arg1}, arg2: {arg2}")

# Print one argv
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Harrison", "Fuller")
print_two_again("Harrison", "Fuller")
print_one("First!")
print_none()

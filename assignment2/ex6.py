# variable of typ_ppl
typ_ppl = 10

# variable of string with variable embedded
x = f"There are {typ_ppl} types of people."

# 2 variables coded as strings
# one variable coded as a string with 2 string variables
bnry = "binary"
do_not = "don't"
y = f"Those who know {bnry} and those who {do_not}."

#prints a variable but out put is a string
print(x)
print(y)

#prints a string with a variable embedded strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

#variable as a condition
hilarious = False

# variable with empty format
jk_eval = "Isn't that joke so funny?! {}"

# prints variable and inserts formated variable condition
print(jk_eval.format(hilarious))

# 2 strings denoted as objects
w = "This is the left side of ..."
e = "a string with a right side."

# prints the addition of e to w
print(w+e)

name = "Harrison D. Fuller"
age = 25
height = 71 # inches
weight = 220 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
cm = 2.54 * height
kg = weight * 0.45


print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#This line is tricky, try to get it exactly right
total = age + height + kg
print(f"If I add {age}, {height}, and {kg} I get {total}.")

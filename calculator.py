# calculator.py

def add(x, y):
    z = x + y
    print("{} + {} = {}".format(x, y, z))
    return z
def sub(x, y):
    z = x - y
    print("{} - {} = {}".format(x, y, z))
    return z
def mult(x, y):
    z = x * y
    print("{} * {} = {}".format(x, y, z))

x = input("Enter a letter: ")
print("You entered {}".format(x))
if x == "a":
    d = add(56, 73)
elif x == "s":
   e = sub(56, 73)
elif x == "m":
    f = mult(56, 73)
else:
    print("The command '{}' is not recognized.".format(x))
print("Done")

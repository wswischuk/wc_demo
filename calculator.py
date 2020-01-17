# calculator.py

def add(x, y):
    z = x + y
    symbol = "+"
    return z, symbol

def sub(x, y):
    z = x - y
    print("{} - {} = {}".format(x, y, z))
    return z
def mult(x, y):
    z = x * y
    if z > 100:
        return z
    print("{} * {} = {}".format(x, y, z))

x = input("Enter a letter: ")
print("You entered {}".format(x))
if x == "a":
    d, f = add(56, 73)
    print("{} {} {} = {}".format(57, f, 73, d))
    if d is None:
       print("I forgot a variable in add()")
elif x == "s":
   e = sub(56, 73)
elif x == "m":
    f = mult(56, 73)
else:
    print("The command '{}' is not recognized.".format(x))
print("Done")

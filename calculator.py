# calculator.py

def add(x, y):
    z = x + y
    symbol = "+"
    return z, symbol

def sub(x, y):
    z = x - y
    symbol = "-"
    return z, symbol
def mult(x, y):
    z = x * y
    symbol = "*"
    return z, symbol
def div(x, y):
    z = x/y
    symbol = "/"
    return z, symbol

x = input("Enter a letter: ")
print("You entered {}".format(x))
if x == "a":
    d, f = add(47, 7)
    print("{} {} {} = {}".format(47, f, 7, d))
    if d is None:
       print("I forgot a variable in add()")
elif x == "s":
   e, g = sub(47, 7)
   print("{} {} {} = {}".format(47, g, 7, e))
   if e is None:
       print("I forgot a variable in add()")
elif x == "m":
    ii, jj = mult(47, 7)
    print("{} {} {} = {}".format(47, jj, 7, ii))
elif x == 'd':
    o, p = div(47, 7)
    print("{} {} {} = {}".format(47, p, 7, o))
else:
    print("The command '{}' is not recognized.".format(x))
print("Done")

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

x = input("Enter First Number: ")
x = float(x)
y = input("Enter Second Number: ")
y = float(y)

L = input("Enter a letter: ")
if L == "a":
    print("You entered {} for addition.".format(L))
    d, f = add(x, y)
    print("{} {} {} = {}".format(x, f, y, d))
    if d is None:
       print("I forgot a variable in add()")
elif L == "s":
   print("You entered {} for subtraction.".format(L))
   e, g = sub(x, y)
   print("{} {} {} = {}".format(x, g, y, e))
   if e is None:
       print("I forgot a variable in add()")
elif L == "m":
    print("You entered {} for multiplication.".format(L))
    ii, jj = mult(x, y)
    print("{} {} {} = {}".format(x, jj, y, ii))
elif L == 'd':
    print("You entered {} for division.".format(L))
    o, p = div(x, y)
    print("{} {} {} = {}".format(x, p, y, o))
else:
    print("The command '{}' is not recognized.".format(L))
print("Done")

# basics
x = input("Enter a letter: ")
print("You entered {}".format(x))
if x == "a":
    a = 1
    b = 2
    c = a + b
    print("{} + {} = {}".format(a, b, c))
elif x == "s":
    a = 20
    b = -3
    c = a - b
    print("{} - {} = {}".format(a, b, c))
elif x == "m":
    a = 5
    b = 20
    c = a*b
    print("{} * {} = {}".format(a, b, c))
else
    print("The command '{}' is not recognized.".format(x))
print("Done")


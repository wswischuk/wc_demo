'''
def open_file():
    try:
        f = open("file_text.txt", 'r')
    except FileNotFoundError:
        print("Fix the code")
        return
    in_line = f.readlines()
    print(in_line)
    f.close()


def main():
    open_file()

if __name__ == '__main__'
    open_file()



# class activity try to generate an error:


def add_numbers(a, b):
    try:
        b = int(b)
        a = int(a)
    except ValueError:
        print("Make sure your values are integer values")
    else:
        print("The addition worked")
        c = b + a
        return c
    return
'''


def add_two_numbers(a, b):
    y = a%1
    z = b%1
    if y == 0 and z == 0:
        c = a + b
        return c
    else:
        raise TypeError("The values {} or {} are not an integer".format(a, b))


if __name__ == "__main__":
    a = 15
    b = 15.3
    c = add_two_numbers(a, b)
    print(c)



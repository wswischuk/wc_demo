import logging


def fibonacci(a, b, fib_list):
    logging.debug("Started fibonacci with a = {} and b = {}"
                  .format(a, b))
    logging.debug("fib_list is {}".format(fib_list))
    next_number = a + b
    fib_list.append(next_number)
    if next_number < 100:
        fibonacci(b, next_number, fib_list)
        logging.warning("going to run again")
    else:
        return
    return fib_list


def main():
    logging.debug("Start main function")
    fib_list = [0, 1]
    fib_list = fibonacci(0, 1, fib_list)
    print(fib_list)


if __name__ == '__main__':
    logging.basicConfig(filename="sequence.log",
                        level=logging.WARNING,
                        filemode='w')
    logging.info("Start Program")
    main()
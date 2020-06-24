# -*- coding: utf-8 -*-
# An algorithm that reads a set of 10 integers, and outputs the value of the sum and the arithmetic mean of them

def main():
    sum = 0
    cont = 0
    total = 10

    for number in range(1, total + 1):
        number = input("Input:")
        if input_is_a_valid_int(number):
            sum += int(number)

        cont = cont + 1

        if cont == total:
            print("Sum:", sum, "Mean:", round(sum / cont, 2))


def input_is_a_valid_int(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Invalid input\n")
        return False


if __name__ == '__main__':
    main()

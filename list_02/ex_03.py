# -*- coding: utf-8 -*-
# Algorithm that reads an integer and shows its square root
import math


def main():

    user_input = input("Number: ")

    if user_input:
        if input_can_be_parsed(user_input) and input_is_a_positive_integer(user_input):
            print("Square root:", math.sqrt(int(user_input)))
            return True
    else:
        print("Empty input \n")
    return False


def input_can_be_parsed(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Invalid input\n")
        return False


def input_is_a_positive_integer(input):
    if int(input) > 0:
        return True
    else:
        print("Invalid interger (only positive numbers are allowed) \n")
        return False


if __name__ == '__main__':
    while True:
        main()

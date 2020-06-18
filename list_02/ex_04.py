# -*- coding: utf-8 -*-

# A pumpkin producer must check the classification of their products for later packaging and sale.
# One of its customers buys only medium sized pumpkins (those with a diameter (d) in the range 15 cm ≤ d <20 cm).
# Develop an algorithm that reads the diameter of a pumpkin and shows whether it is of the average type or not.
# If it does not fit the classification, inform “product out of measure”

import math


def main():

    user_input = input("Diameter: ")

    if user_input:
        if input_can_be_parsed(user_input) and input_is_a_positive_integer(user_input):
            if(int(user_input) >= 15 and int(user_input) <= 20):
                print("Correct product measure")
            else:
                print("Product out of measure")
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
    if int(input) >= 0:
        return True
    else:
        print("Invalid interger (only positive numbers are allowed) \n")
        return False


if __name__ == '__main__':
    while True:
        main()

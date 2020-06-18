# -*- coding: utf-8 -*-
# In a certain stationery, the photocopy costs R$ 0.25, if less than 100 copies are made.
# From 100 copies, the value of each photocopy taken drops to R$ 0.20.
# Develop an algorithm that reads the number of copies and shows the amount to pay for the service.


def main():
    user_input = input("Number of copies: ")

    if user_input:
        if input_can_be_parsed(user_input) and input_is_a_positive_integer(user_input):
            copies = int(user_input)
            if copies < 100:
                cost = copies * 0.25
            else:
                cost = copies * 0.20

            print("Total cost: ", round(cost, 2))
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

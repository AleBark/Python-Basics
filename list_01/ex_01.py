# -*- coding: utf-8 -*-
# Algorithm that reads an integer and shows its predecessor and successor.

def main():

    user_input = input("Enter your value: ")

    if user_input:
        if input_can_be_parsed(user_input):
            print("The predecessor is:", int(user_input) - 1,
                  "and the successor is:", int(user_input) + 1, "\n")
        return True
    else:
        print("Empty input \n")
        return False


def input_can_be_parsed(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Invalid input \n")
        return False


if __name__ == '__main__':
    while True:
        main()

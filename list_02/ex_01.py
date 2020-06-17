# -*- coding: utf-8 -*-
# Algorithm that reads an integer and checks whether it is even or odd

def main():

    user_input = input("Enter your value: ")

    if user_input:
        if input_can_be_parsed(user_input):
            if (int(user_input) % 2) == 0:
                print("{0} is Even".format(user_input))
            else:
                print("{0} is Odd".format(user_input))
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

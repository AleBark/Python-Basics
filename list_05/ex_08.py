# -*- coding: utf-8 -*-
# An algorithm that (given a non-negative integer n) checks if n is triangular

def main():
    user_input = input('Input: ')
    i = 1
    total = 0

    if input_is_a_valid_int(user_input) and input_is_a_valid_number(user_input):
        user_input = int(user_input)

        while total < user_input:
            total = i * (i + 1) * (i + 2)
            i += 1

        if total == user_input:
            print('Triangular')
        else:
            print('Not triangular')


def input_is_a_valid_int(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Invalid input\n")
        return False


def input_is_a_valid_number(input):
    return int(input) > 0


if __name__ == '__main__':
    while True:
        main()

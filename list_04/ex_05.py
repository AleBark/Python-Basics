# -*- coding: utf-8 -*-
# Algorithm that prints the odd numbers from 1 to n, where n is provided by the user

def main():
    end_rage = input("Input: ")
    if input_is_a_valid_int(end_rage):
        end_rage = int(end_rage)
        for number in range(1, end_rage):
            if number % 2 != 0:
                print(number)


def input_is_a_valid_int(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Invalid input\n")
        return False


if __name__ == '__main__':
    while True:
        main()

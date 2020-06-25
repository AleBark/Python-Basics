# -*- coding: utf-8 -*-
# An algorithm that reads three numbers from the keyboard and checks whether the first is greater than the sum
# of the other two

def main():
    input_list = []
    print("Starting")
    for idx in range(1, 4):
        integer = input("Input: ")

        if input_is_a_valid_int(integer):
            input_list.append(integer)
        else:
            break

        if len(input_list) == 3:
            sum = input_list[0] + input_list[1]
            if sum > input_list[2]:
                print("First integer is bigger than the sum of the other 2")
            else:
                print("First integer is not bigger than the sum of the other 2")


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

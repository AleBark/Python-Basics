# -*- coding: utf-8 -*-
# An algorithm that reads 4 whole numbers and calculates the sum of those that are even.

def main():
    input_list = []
    print("----------")
    for idx in range(1, 4):
        integer = input("Input: ")

        if input_is_a_valid_int(integer):
            if int(integer) % 2 == 0:
                input_list.append(int(integer))
        else:
            break
    print(sum(input_list))


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

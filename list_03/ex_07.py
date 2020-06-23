# -*- coding: utf-8 -*-
# An algorithm that reads three integers and shows them in descending order.

def main():
    first_integer = input("First value: ")
    second_integer = input("Second value: ")
    third_integer = input("Third value: ")

    if first_integer and second_integer and third_integer:
        if input_is_a_valid_int(first_integer) and input_is_a_valid_int(second_integer) and input_is_a_valid_int(
                third_integer):
            if first_integer >= second_integer:
                if first_integer >= third_integer:
                    if second_integer >= third_integer:
                        print(first_integer, ' ', second_integer, ' ', third_integer)
                    else:
                        print(first_integer, ' ', third_integer, ' ', second_integer)
                else:
                    print(third_integer, ' ', first_integer, ' ', second_integer)
            else:
                if second_integer >= third_integer:
                    if third_integer >= first_integer:
                        print(second_integer, ' ', third_integer, ' ', first_integer)
                    else:
                        print(second_integer, ' ', first_integer, ' ', third_integer)
                else:
                    print(third_integer, ' ', second_integer, ' ', first_integer)
        return True
    else:
        print("Empty input \n")
        return False


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

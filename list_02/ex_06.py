# -*- coding: utf-8 -*-
# Given the height (h) and the sex of a person (1 for male and 2 for female)
# Develop an algorithm that calculates the user's ideal weight (p) using the following formulas:
# 1. For men: p = (72.7 * h) -58
# 2. For women: p = (62.1 * h) -44.7

def main():
    height = input("Height: ")
    sex = input("Sex: ")

    if height and sex:
        if input_is_a_valid_int(sex) and input_is_a_valid_sex(sex) and input_is_a_valid_height(height):

            if int(sex) == 1:
                result = (72.7 * float(height)) - 58
            else:
                result = (62.1 * float(height)) - 44.7

            print("Ideal weight: ", round(result, 2))
            return True
    else:
        print("Empty input \n")
        return False


def input_is_a_valid_height(input):
    try:
        float(input)
        return True
    except ValueError:
        print("Invalid height\n")
        return False


def input_is_a_valid_int(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Invalid sex\n")
        return False


def input_is_a_valid_sex(input):
    if int(input) in range(1, 3):
        return True
    else:
        print("Invalid sex (accepted range: 1-2) \n")
        return False


if __name__ == '__main__':
    while True:
        main()

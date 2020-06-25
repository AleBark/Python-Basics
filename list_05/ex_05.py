# -*- coding: utf-8 -*-
# An algorithm that reads two real values ​​from the keyboard and prints on the screen:
# 1. The sum of these values
# 2. Their product
# 3. The quotient between them

def main():
    input_list = []
    print("\n ----------")
    for idx in range(1, 3):
        user_input = input("\n Input: ")
        if input_is_a_valid_float(user_input) and input_is_a_valid_number(user_input):
            user_input = float(user_input)
            input_list.append(user_input)
        else:
            break

        if len(input_list) == 2:
            sum = round(input_list[0] + input_list[1], 2)
            product = round(input_list[0] * input_list[1], 2)
            quotient = round(input_list[0] / input_list[1], 2)
            print("\n Sum:", sum, "\n Product:", product, "\n Quotient:", quotient, "\n")


def input_is_a_valid_float(input):
    try:
        float(input)
        return True
    except ValueError:
        print("Invalid input\n")
        return False


def input_is_a_valid_number(input):
    return float(input) != 0


if __name__ == '__main__':
    while True:
        main()

# -*- coding: utf-8 -*-
# Algorithm that receives a person's salary and calculates how many minimum
# wages this value represents

def main():
    minimum_wage_value = 1045
    user_input = input("Wage: ")

    if user_input:
        if input_can_be_parsed(user_input):
            print("Minimum wage quantity: ", round(
                float(user_input)/minimum_wage_value, 2), "\n")
            return True
    else:
        print("Empty input \n")
    return False


def input_can_be_parsed(input):
    try:
        float(input)
        return True
    except ValueError:
        print("Invalid input\n")
        return False


if __name__ == '__main__':
    while True:
        main()

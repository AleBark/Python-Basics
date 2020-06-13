# -*- coding: utf-8 -*-
# Algorithm that receives a person's salary and calculates how many minimum
# wages this value represents

def main():
    minimum_wage_value = 1045
    wage = input("Wage: ")

    if wage:
        if input_can_be_parsed(wage):
            print("Minimum wage quantity: ", round(
                float(wage)/minimum_wage_value, 2), "\n")
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

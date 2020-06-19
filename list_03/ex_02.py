# -*- coding: utf-8 -*-
# The BMI, body mass index, is calculated using the following formula: BMI = mass / height**2
# Develop an algorithm that reads the user's mass (in kilograms) and height (in meters) and shows the BMI value
# and what his condition is according to the criteria presented in the WHO (World Health Organization) table

def main():

    height = input("Height in meters: ")
    weight = input("Weight in kg: ")

    if height and weight:
        if input_is_a_valid_float(weight) and input_is_a_valid_float(height):
            bmi = float(weight)/(float(height) ** 2)
            if bmi < 18.5:
                print("Underweight")
            elif bmi >= 18.5 and bmi < 25:
                print("Normal weight")
            elif bmi >= 25:
                print("Overweight")
    else:
        print("Empty input \n")
        return False


def input_is_a_valid_float(input):
    try:
        float(input)
        return True
    except ValueError:
        print("Invalid height \n")
        return False


if __name__ == '__main__':
    while True:
        main()

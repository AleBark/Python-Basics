# -*- coding: utf-8 -*-
# From the information in the table below, develop an algorithm that reads the weight in kg of a boxer
# and shows which category he belongs to. If it does not fit, enter "Category lower than Middleweight".
# Remembering that 1 kilogram = 2.20462262 pounds.
# X   - 160         | Lower than Middleweight
# 161 - 168         | Middleweight
# 169 - 175         | Light heavyweight,
# 176 - 200         | Cruiserweight,
# 201 lb or greater | Heavyweight
####

def main():
    user_input = input("Weight (kg): ")

    if user_input:
        if input_is_a_valid_float(user_input):
            kg_weight = float(user_input)
            lb_weight = kg_weight * 2.2046

            if 161 <= lb_weight <= 168:
                print("Super middleweight")
            elif 169 <= lb_weight <= 175:
                print("Light heavyweight")
            elif 176 <= lb_weight <= 200:
                print("Cruiserweight")
            elif lb_weight >= 201:
                print("Heavyweight")
            else:
                print("Category lower than Middleweight")
        return True
    else:
        print("Empty input \n")
        return False


def input_is_a_valid_float(input):
    try:
        float(input)
        return True
    except ValueError:
        print("Invalid entry \n")
        return False


if __name__ == '__main__':
    while True:
        main()

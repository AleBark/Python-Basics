# -*- coding: utf-8 -*-
# Algorithm that calculates the amount of paint cans needed to paint a cylinder tank, where its height and radius is provided.
# Considering the following data:
# 1.The paint can costs R$ 50.00
# 2.Each can contains 5 liters
# 3.Each liter of paint paints 3 square meters.
# 4.User input: height and radius of the cylinder.
# 5.Outputs number of cans and its costs

def main():

    height = input("Cylinder height: ")
    radius = input("Cylinder radius: ")
    pi = 3.1415
    can_cost = 50.00

    if height and radius:
        if input_can_be_parsed(height) and input_is_greater_than_zero(height) and input_is_greater_than_zero(radius) and input_can_be_parsed(radius):

            base_area = pi * pow(float(radius), 2)
            side_area = 2 * pi * float(radius) * float(height)
            total_area = 2 * base_area + side_area

            total_liters = total_area / 3.0
            cans_quantity = total_liters / 5.0

            print('Cans quantity: ', round(cans_quantity, 2),
                  " total cost: ", round(cans_quantity * can_cost, 2))

            return True
        else:
            print("Invalid input \n")
    else:
        print("Empty input \n")
    return False


def input_is_greater_than_zero(input):
    try:
        return float(input) > 0
    except ValueError:
        print("Invalid input\n")
        return False


def input_can_be_parsed(input):
    try:
        float(input)
        return True
    except ValueError:
        print("Invalid input\n")
        return False

    # float precolata, altura, arealateral, areadabase, areatotal, custo;
    # int raio, quantidadelatas;

    # scanf("%f",&precolata);
    # scanf("%d",&raio);
    # scanf("%f",&altura);


if __name__ == '__main__':
    while True:
        main()

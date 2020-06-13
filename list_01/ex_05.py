# -*- coding: utf-8 -*-
# Algorithm that calculates the average consumption of a car (measured in km/l),
# taking as input the total distance traveled (KM) and the volume of fuel consumed
# to travel it.

def main():
    total_distance = input("Total distance (km): ")
    fuel_consumed = input("Fuel consumed (L): ")

    if total_distance and fuel_consumed:
        if input_can_be_parsed(total_distance) and input_is_greater_than_zero(total_distance) and input_is_greater_than_zero(fuel_consumed) and input_can_be_parsed(fuel_consumed):

            print("Average: ", round(
                (float(total_distance) / float(fuel_consumed)), 2))
            return True
        else:
            print("Invalid input \n")
    else:
        print("Empty input \n")
    return False


def input_is_greater_than_zero(product_value):
    try:
        return int(product_value) > 0
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


if __name__ == '__main__':
    while True:
        main()

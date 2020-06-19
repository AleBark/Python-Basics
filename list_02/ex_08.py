# -*- coding: utf-8 -*-
# In a given parking lot, the first hour costs R$ 8.00, which is the minimum amount charged. After one hour the amount is reduced, R$ 1.50 every 15 minutes.
# Develop an algorithm that reads an integer corresponding to the number of minutes used in the parking lot and displays the message
# “Minimum value, R$ 8.00” or “Fractional value, R$ x”, in which x will be the amount to be paid calculated by the algorithm


def main():

    spent_time = input("Spent time in minutes: ")
    hour_cost = 8.00
    if spent_time:
        if input_is_a_valid_int(spent_time) and input_is_a_positive_int(spent_time):
            if int(spent_time) > 60:
                fracional_time = int(spent_time) - 60
                fifteen_min_chunks = fracional_time / 15
                if int(fifteen_min_chunks) > 0:
                    print("Total cost:", round(hour_cost +
                                               (1.50 * int(fifteen_min_chunks)), 2))
                else:
                    print("Total cost:", hour_cost)
            else:
                print("Minimum value:", hour_cost)
    else:
        print("Empty input \n")
        return False


def input_is_a_positive_int(input):
    return int(input) > 0


def input_is_a_valid_int(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Invalid entry \n")
        return False


if __name__ == '__main__':
    while True:
        main()

# -*- coding: utf-8 -*-
# Algorithm that receives the value of a product and calculate the following values:
# (1) cash with 5% discount;
# (2) the value of the installment in 2x;
# (3) the value of the installment in 3x with a 5% increase.

def main():

    user_input = input("Product value: ")

    if user_input:
        if input_can_be_parsed(user_input) and input_is_greater_than_zero(user_input):
            user_input_float = float(user_input)

            print("Cash with 5% discount: ", user_input_float -
                  percentage(5, user_input_float), "\n")

            print("The value of the installment in 2x :",
                  user_input_float/2, "\n")

            print("The value of the installment in 3x with a 5% increase:",
                  (user_input_float + percentage(5, user_input_float)) / 3, "\n")
            return True
    else:
        print("Empty input \n")
    return False


def percentage(part, whole):
    return 100 * part / float(whole)


def input_is_greater_than_zero(user_input):
    return int(user_input) > 0


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

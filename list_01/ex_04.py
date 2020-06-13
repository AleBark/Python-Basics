# -*- coding: utf-8 -*-
# Algorithm that receives the value of a product and calculate the following values:
# (1) cash with 5% discount;
# (2) the value of the installment in 2x;
# (3) the value of the installment in 3x with a 5% increase.

def main():

    product_value = input("Product value: ")

    if product_value:
        if input_can_be_parsed(product_value) and input_is_greater_than_zero(product_value):
            product_value_float = float(product_value)

            print("Cash with 5% discount: ", round((product_value_float -
                  percentage(5, product_value_float), 2), "\n")

            print("The value of the installment in 2x :",
                  round((product_value_float/2), 2), "\n")

            print("The value of the installment in 3x with a 5% increase:",
                 round((product_value_float + percentage(5,
                       product_value_float), 2 / 3), 2), "\n")
            return True
    else:
        print("Empty input \n")
    return False


def percentage(part, whole):
    return 100 * part / float(whole)


def input_is_greater_than_zero(product_value):
    return int(product_value) > 0


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

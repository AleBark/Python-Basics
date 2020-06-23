# -*- coding: utf-8 -*-
# At a given appliance store, products can be purchased as follows
# 1x - 8% discount
# 2x - 4% discount
# 3x - 0% discount
# 4x - 4% addition
# Develop an algorithm that reads the customer's option and outputs
# the price the discount / addition

def main():
    product_price = input("Price: ")
    installment_quantity = input("Installment Quantity: ")

    if product_price and installment_quantity:
        if input_is_a_valid_int(installment_quantity) and input_is_a_valid_float(product_price):
            product_price = float(product_price)
            installment_quantity = int(installment_quantity)
            if installment_quantity == 1:
                discount = (product_price * 0.08)
                print("Final price: 1x", round(product_price - discount, 2))
            elif installment_quantity == 2:
                discount = (product_price * 0.04) / 2
                print("Final price: 2x - ", round((product_price / 2) - discount, 2))
            elif installment_quantity == 3:
                print("Final price: 3x - ", (round(product_price / 3), 2))
            elif installment_quantity == 4:
                addition = (product_price * 0.04) / 4
                print("Final price: 4x -", round((product_price / 4) + addition), 2)
            else:
                print("Invalid installment number")
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


def input_is_a_valid_int(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Invalid sex\n")
        return False


if __name__ == '__main__':
    while True:
        main()

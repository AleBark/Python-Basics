# -*- coding: utf-8 -*-
# An algorithm that receives the value of the account and the amount paid and returns the change
# in Brazilian notes and coins


def main():
    bill_value = input("Bill value:")
    amount = input("Amount paid:")

    if bill_value and amount:
        if input_is_a_valid_float(bill_value) and input_is_a_valid_number(bill_value) and input_is_a_valid_float(
                amount) and input_is_a_valid_number(amount):

            amount = float(amount)
            bill_value = float(bill_value)

            if amount < bill_value:
                print("Insufficient amount")
                return False
            else:
                change = amount - bill_value
                change_calculator(change)
                return True
        return True
    else:
        print("Empty input \n")
        return False


def change_calculator(change):
    posible_changes = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.5, 0.1]
    changes_quantity = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Total change:", change, '\n')
    if change != 0:
        for x in range(len(posible_changes)):
            cont = 0
            while change >= posible_changes[x]:
                change = change - posible_changes[x]
                cont += 1
                changes_quantity[x] = cont
    print(posible_changes, '-', changes_quantity)


def input_is_a_valid_float(input):
    try:
        float(input)
        return True
    except ValueError:
        print("Invalid input\n")
        return False


def input_is_a_valid_number(input):
    return float(input) > 0


if __name__ == '__main__':
    while True:
        main()

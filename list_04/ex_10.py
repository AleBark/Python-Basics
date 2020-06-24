# -*- coding: utf-8 -*-
# A foreign exchange company allows the purchase of dollars, pounds and euros. Develop an algorithm that reads the code
# of the currency the customer wants to buy and the amount he wants to purchase in that currency. Then show how much he
# should pay in reais to complete the operation. In addition to the quotation, the company charges a commission of 5%
# (when the value is less than R$ 1,000), or 3% (when greater or equal to R$ 1,000).
# Consider the exchange rate for the day.

def main():
    currency = input("Currencies (1) Dollars, (2) Pounds, (3) Euros: ")
    amount = input("Amount: ")

    euro_rate = 5.83
    dollar_rate = 5.15
    pound_rate = 6.46

    if currency:
        if input_is_a_valid_int(currency) and input_is_a_valid_currency(currency):
            if input_is_a_valid_amount(amount):
                commission = 0.05
                if float(amount) >= 1000:
                    commission = 0.03
                if int(currency) == 1:
                    total = float(amount) * dollar_rate
                elif int(currency) == 2:
                    total = float(amount) * pound_rate
                else:
                    total = float(amount) * euro_rate
                print("You should pay", round(total + (total * commission), 2), "real(is)")
            else:
                print("Invalid amount")
                return False
    return True


def input_is_a_valid_currency(input):
    if int(input) in range(1, 4):
        return True
    else:
        print("Invalid currency (accepted values: 1 - 3) \n")
        return False


def input_is_a_valid_amount(input):
    try:
        float(input)
        return True
    except ValueError:
        print("Invalid input\n")
        return False


def input_is_a_valid_int(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Invalid input\n")
        return False


if __name__ == '__main__':
    while True:
        main()

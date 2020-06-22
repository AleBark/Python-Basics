# -*- coding: utf-8 -*-
# Develop an algorithm that, given the age of a swimmer, shows its classification according to one of the following categories:
# • 5 to 7 years: Infant A;
# • 8 to 10 years old: Infant B;
# • 11 to 13 years old: Juvenile A;
# • 14 to 17 years old: Juvenile B;
# • Over 18 years old: Adult.

def main():
    user_input = input("Age: ")

    if user_input:
        if input_is_a_valid_int(user_input) and input_is_a_valid_age(user_input):
            age = int(user_input)
            if 5 <= age <= 7:
                print("Infant A")
            elif 8 <= age <= 10:
                print("Infant B")
            elif 11 <= age <= 13:
                print("Juvenile A")
            elif 14 <= age <= 17:
                print("Juvenile B")
            else:
                print("Adult")
        return True
    else:
        print("Empty input \n")
        return False


def input_is_a_valid_int(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Invalid entry \n")
        return False


def input_is_a_valid_age(input):
    if int(input) in range(5, 101):
        return True
    else:
        print("Invalid age (accepted range: 4-100) \n")
        return False


if __name__ == '__main__':
    while True:
        main()

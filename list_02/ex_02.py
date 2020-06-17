# -*- coding: utf-8 -*-
# Algorithm that reads a person's birthdate and calculates its age in 2021 and checks if that person can get a driver's license or not

def main():

    birthdate = input("Birthdate: ")

    if birthdate:
        if input_can_be_parsed(birthdate) and input_is_a_valid_date(birthdate):
            person_age = 2021 - int(birthdate)
            print("Person age in 2021: ", person_age, "\n")

            if person_age >= 18:
                print("That person can get a driver's license in 2021\n")
            else:
                print("That person can not get a driver's license in 2021 \n")
            return True
    else:
        print("Empty input \n")
    return False


def input_can_be_parsed(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Invalid input\n")
        return False


def input_is_a_valid_date(input):
    if int(input) in range(1900, 2021):
        return True
    else:
        print("Invalid year (accepted range: 1900-2020) \n")
        return False


if __name__ == '__main__':
    while True:
        main()

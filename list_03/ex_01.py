# -*- coding: utf-8 -*-
# Develop an algorithm that informs your electoral situation, knowing that:
# A person who has < 16 years do not vote
# Voting is optional for adults between 16 and 18, or over 65 years
# Voting is mandatory for adults between 18 and 65


def main():
    age_input = input("Input: ")

    if age_input:
        if input_can_be_parsed(age_input):
            age = int(age_input)
            if age < 16:
                print("You can not vote yet")
            elif 16 <= age < 18:
                print("You can vote")
            elif 18 <= age <= 65:
                print("You have to vote")
            elif age > 65:
                print("You can vote")
            else:
                print("Invalid value")
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


if __name__ == '__main__':
    while True:
        main()

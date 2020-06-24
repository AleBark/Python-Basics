# -*- coding: utf-8 -*-
# An algorithm that plays Rock-paper-scissor with the user;
# The algorithm needs to randomly chooses his "move", read the user's option and output the result:
# "computer won", "user won" or "draw"
import random


def main():
    user_input = input("(1) Rock , (2) Paper, (3) Scissor: ")

    if user_input:
        if input_is_a_valid_int(user_input) and input_is_a_valid_move(user_input):
            user_input = int(user_input)
            computer_input = random.randint(1, 3)
            print("Computer move: ", computer_input)
            if user_input == 1:
                if computer_input == 1:
                    print("Draw")
                elif computer_input == 2:
                    print("Computer Won")
                else:
                    print("User Won")
            elif user_input == 2:
                if computer_input == 1:
                    print("User Won")
                elif computer_input == 2:
                    print("Draw")
                else:
                    print("Computer Won")
            else:
                if computer_input == 1:
                    print("Computer Won")
                elif computer_input == 2:
                    print("User Won")
                else:
                    print("Draw")
    else:
        print("Empty input \n")


def input_is_a_valid_move(input):
    if int(input) in range(1, 4):
        return True
    else:
        print("Invalid move (accepted values: 1 - 3) \n")
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

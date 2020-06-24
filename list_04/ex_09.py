# -*- coding: utf-8 -*-
# An algorithm that prints the multiple numbers of 3 between in (initial limit) and fl (final limit).
# Values li and lf must be informed by the user (they cannot belong to the range)

def main():
    i_limit = input("Initial limit: ")
    f_limit = input("Final limit: ")

    if i_limit and f_limit:
        if input_is_a_valid_int(i_limit) and input_is_a_valid_int(f_limit):
            for number in range(int(i_limit) + 1, int(f_limit) + 1):
                if number % 3 == 0:
                    print(number)


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

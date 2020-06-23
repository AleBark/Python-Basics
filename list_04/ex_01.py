# -*- coding: utf-8 -*-
# Algorithm that prints the numbers from 1 to 99, with an increment of 2. Example: 1, 3, 5 ..... 97, 99

def main():
    for number in range(1, 101):
        if number % 2 != 0:
            print("{0}".format(number))


if __name__ == '__main__':
    main()

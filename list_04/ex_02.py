# -*- coding: utf-8 -*-
# Algorithm that prints the numbers from 50 to 0 with a decrement of 5. Example: 50, 45, 40 ..... 5, 0

def main():
    for number in range(50, -1, -5):
        print("{0}".format(number))


if __name__ == '__main__':
    main()

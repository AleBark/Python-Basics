# -*- coding: utf-8 -*-
# Algorithm that prints the numbers from -100 to 100, in increments of 10. Example: -100, -90, -80 ..... 90, 100

def main():
    for number in range(-100, 101, 10):
        print("{0}".format(number))


if __name__ == '__main__':
    main()

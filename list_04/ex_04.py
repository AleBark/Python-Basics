# -*- coding: utf-8 -*-
# Algorithm that prints the multiple numbers multiple of 4 in the range of 1 to 100

def main():
    for number in range(1, 101):
        if number % 4 == 0:
            print(number)


if __name__ == '__main__':
    main()

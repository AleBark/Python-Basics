# -*- coding: utf-8 -*-
# Algorithm that prints an inch-to-centimeter conversion table, which ranges from 1 to 20 inches.


def main():
    for number in range(1, 21):
        print(number, "in = ", round(number * 2.54, 2), "cm")

if __name__ == '__main__':
    main()

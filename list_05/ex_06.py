# -*- coding: utf-8 -*-
# An algorithm that orders a list of 100 randomly generated integers
import random


def main():
    integer_list = []
    for cont in range(0, 101):
        number = random.randint(1, 100)
        integer_list.append(number)
    print("Unsorted", integer_list)

    cont = 0
    while cont < len(integer_list):
        key = cont
        j = cont + 1
        while j < len(integer_list):
            if integer_list[key] > integer_list[j]:
                key = j
            j += 1
        integer_list[cont], integer_list[key] = integer_list[key], integer_list[cont]
        cont += 1
    print("Sorted", integer_list)


if __name__ == '__main__':
    main()

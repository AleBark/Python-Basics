# -*- coding: utf-8 -*-
# An algorithm that shows the multiplication table from 1 to 10, storing each value in a list.

def main():
    integer_list = []

    for idx in range(1, 11):
        result = 1 * idx
        integer_list.append(result)
        print("1 * ", idx, '=', result)
    print(integer_list)


if __name__ == '__main__':
    main()

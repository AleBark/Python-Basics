# -*- coding: utf-8 -*-
# An algorithm that shows the multiplication table from 1 to 10, using only one repetition loop.

def main():
    integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for idx in range(len(integer_list)):
        print("1 * ", integer_list[idx], '=', 1 * integer_list[idx])


if __name__ == '__main__':
    main()

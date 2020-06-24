# -*- coding: utf-8 -*-
# An algorithm that prints a conversion table from meters (m) to miles (mi),
# from 20 km to 160 km, every 10 kilometers

def main():
    for km in range(20, 161, 10):
        print(km * 1000, "Meters (", km, "Kms) is equivalent to", round(km * 0.621371, 2), "miles")


if __name__ == '__main__':
    main()

# !/usr/bin/env python3
# Created by: Nolan Shami
# Created on: Dec 12th, 2022
# This program compute the cosine of x.

import math


def cal_cosine(x):
    degrees = x
    cosine_x = 1
    sign = -1
    for i in range(2, 10, 2):
        y = x * (math.pi / 180)
        cosine_x = cosine_x + (sign * (y**i)) / math.factorial(i)
        sign = -sign

    # print cosine
    print("The value of cos({0}) = {1:.4f}".format(degrees, cosine_x))


def main():
    # get x from the user
    x_string = input("Enter the value of x (in degrees): ")
    try:
        x = float(x_string)
        cal_cosine(x)
    except Exception:
        print("Come on man...THAT'S TOO EASY...enter a valid number.")


if __name__ == "__main__":
    main()

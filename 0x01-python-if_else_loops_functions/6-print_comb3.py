#!/usr/bin/python3
for digit_10s in range(9):
    for digit_1s in range(digit_10s + 1, 10):
        if digit_10s < 8:
            print("{:d}{:d}".format(digit_10s, digit_1s), end=", ")
        else:
            print("{:d}{:d}".format(digit_10s, digit_1s))

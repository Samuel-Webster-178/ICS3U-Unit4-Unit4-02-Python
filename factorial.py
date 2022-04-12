#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program includes a while loop


def main():
    # I calculate circumference

    # input
    string_integer = input("Enter your highest positive integer: ")
    answer = 1
    i = 1

    # process & output
    try:
        int_integer = int(string_integer)
        if int_integer == 0:
            answer = 1
        elif int_integer < 0:
            answer = "undefined"
        else:
            while i <= int_integer:
                answer *= i
                i += 1
        print("{0}! = {1}".format(int_integer, answer))
    except Exception:
        print("Invalid Input")
    print("\nDone.")


if __name__ == "__main__":
    main()

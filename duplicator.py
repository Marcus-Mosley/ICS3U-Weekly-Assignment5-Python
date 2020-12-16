#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on December 2020
# This program duplicates characters in a string


def main():
    # This function duplicates characters in a string

    # Input
    string = input("Please enter a String: ")

    while True:
        num_chars_str = input("Please enter the desired number of characters"
                              " to be duplicated: ")
        try:
            num_chars_int = int(num_chars_str)
        except Exception:
            print("That is not an integer, please input a number!")
            print("")
        else:
            if num_chars_int <= 0:
                print("That is not a valid input, please input a number"
                      " greater than 0!")
                print("")
            else:
                break
    while True:
        duplicate_str = input("Please enter the desired number of"
                              " duplications: ")

        try:
            duplicate_int = int(duplicate_str)
        except Exception:
            print("That is not an integer, please input a number!")
            print("")
        else:
            if duplicate_int <= 0:
                print("That is not a valid input, please input a number"
                      " greater than 0!")
                print("")
            else:
                break
    print("")

    # Process & Output
    counter_duplicate = 0
    while counter_duplicate < duplicate_int:
        counter_chars = 0
        while counter_chars < num_chars_int:
            print(string[counter_chars], end='')
            counter_chars += 1
        counter_duplicate += 1


if __name__ == "__main__":
    main()

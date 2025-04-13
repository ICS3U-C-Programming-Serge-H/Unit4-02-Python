#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: Mar 28, 2025
# This program will ask the user for a positive integer
# and then calculate The sum of a the factorial number


def factorial_program():
    # Get user number

    while True:
        try:
            user_number = input("Enter a whole number positive number: ")
            number = int(user_number)
            if number < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid number, Please enter a whole number.")

    factorial = 1
    i = 1
    while i <= number:
        factorial *= i
        i += 1

    print(f"The factorial of {number} is {factorial}")


if __name__ == "__main__":
    factorial_program()

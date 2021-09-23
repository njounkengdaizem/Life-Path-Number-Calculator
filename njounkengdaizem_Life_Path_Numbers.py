#################################################################################
# Author: Daize Njounkeng
# Username:njounkengdaizem
#
# Assignment: A04-A Bug's Life
# Purpose: To create a program for the life path number problem
# Definition: This life Path Number Calculator Computes the Life Path Number or users
# And returns their  characteristics
# Life Path number Source: https://seventhlifepath.com/
#################################################################################
import time
import webbrowser


def month(num):
    """
    asks for user's birth month and checks if it is a master or not.
    If not convert the input to digits and return the sum of the digits.
    """
    # Tests for inputs greater than or equal 13, since no months exists above 12
    if int(num) > 12:
        print("Error! Enter the month number in the range 1 to 12:")
        int(input("Enter the number of your birth month. For example, July would be 7:"))
    else:
        pass
    return int(num)


def day(dayin):
    """
    asks for the users date of birth and checks if it is a master or not.
    If not convert the input to digits and return the sum of the digits.
    """

    # Tests for inputs greater than or equal 13, since no months exists above 12

    if int(dayin) > 31:
        print("Error! Enter a new number:")
        dayin = (input("enter the number of your birth day:"))
    else:
        pass
    return int(dayin)


def year(yearin):
    """ asks for the users birth year and adds the digits together and checks if it's a master or not.
    If not convert the input to digits and return the sum of the digits."""

    # Tests for inputs greater than or equal 13, since no months exists above 12

    if len(yearin) == 4:
        pass
    else:
        print("Error! Enter a new number:")
        yearin = int(input("enter the number of your birth year:"))
    return int(yearin)


def calculate(life):
    life1 = 0
    if life % 11 == 0:
        return life
    else:
        for i in str(life):
            life1 = life1 + int(i)
        return life1


def comments(com):
    """Provides comments to the user based on their Life Path Number"""
    if com == 1:
        print("Wait for the magic!")
        time.sleep(3)
        webbrowser.open("https://seventhlifepath.com/numerology/life-path-number-1/")
    elif com == 2:
        print("Wait for the magic!")
        time.sleep(3)
        webbrowser.open("https://seventhlifepath.com/numerology/life-path-number-2/")
    elif com == 3:
        print("Wait for the magic!")
        time.sleep(3)
        webbrowser.open("https://seventhlifepath.com/numerology/life-path-number-3/")
    elif com == 4:
        print("Wait for the magic!")
        time.sleep(3)
        webbrowser.open("https://seventhlifepath.com/numerology/life-path-number-4/")
    elif com == 5:
        print("Wait for the magic!")
        time.sleep(3)
        webbrowser.open("https://seventhlifepath.com/numerology/life-path-number-5/")
    elif com == 6:
        print("Wait for the magic!")
        time.sleep(3)
        webbrowser.open("https://seventhlifepath.com/numerology/life-path-number-6/")
    elif com == 7:
        print("Wait for the magic!")
        time.sleep(3)
        webbrowser.open("https://seventhlifepath.com/numerology/life-path-number-7/")
    elif com == 8:
        print("Wait for the magic!")
        time.sleep(3)
        webbrowser.open("https://seventhlifepath.com/numerology/life-path-number-8/")
    elif com == 9:
        print("Wait for the magic!")
        time.sleep(3)
        webbrowser.open("https://seventhlifepath.com/numerology/life-path-number-9/")
    elif com == 11:
        print("Wait for the magic!")
        time.sleep(3)
        webbrowser.open("https://seventhlifepath.com/numerology/life-path-number-11/")
    elif com == 22:
        print("Wait for the magic!")
        time.sleep(3)
        webbrowser.open("https://seventhlifepath.com/numerology/life-path-number-22/")
    elif com == 33:
        print("Wait for the magic!")
        time.sleep(3)
        webbrowser.open("https://seventhlifepath.com/numerology/life-path-number-33/")
    else:
        print("Sorry your number doesn't exist, a unique being indeed!")


def main():
    """call all the previously defined functions to the main.
    Collects input statements from the user and passes its parameter to the functions. """
    monthnum = int(input("Howdy, Please enter your birth month. For example, July would be 7:"))
    first_val = month(monthnum)
    first_val = calculate(first_val)
    print(first_val)
    daynum = int(input("One step closer. Now enter the number of your birth day:"))
    second_val = day(daynum)
    second_val = calculate(second_val)
    print(second_val)
    yearnum = (input("Please enter the number of your birth year:"))
    int(yearnum)
    third_val = year(yearnum)
    third_val = calculate(third_val)
    print(third_val)
    total = int(first_val + second_val + third_val)
    life_path = calculate(total)
    print("Your life path number is {}" .format(life_path))
    comments(life_path)


main()

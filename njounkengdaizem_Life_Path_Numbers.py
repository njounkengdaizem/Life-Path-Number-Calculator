#################################################################################
# Author: Merville Njounkeng

# Purpose: To create a program for the life path number problem

# Definition: This life Path Number Calculator Computes the Life Path Number or users

# And returns their  characteristics
#################################################################################



def month(num):
    """
    asks for user's birth month and checks if it is a master or not.
    If not convert the input to digits and return the sum of the digits.
    """

    # Tests for inputs greater than or equal 13, since no months exists above 12

    if int(num) > 12:
        print("Error! Enter the month number in the range 1 to 12:")
        num = (input("enter the number of your birth month. For example, July would be 7:"))
    else:
        pass

    if int(num) % 11 == 0:
        addnum = 11
    elif int(num) < 10:
        addnum = int(num)
    else:
        num1 = num[0:1]
        num2 = num[1:2]
        addnum = int(num1) + int(num2)
    print(addnum)
    return addnum


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

    if int(dayin) % 11 == 0:
        addnum2 = int(dayin)
    elif int(dayin) < 10:
        addnum2 = int(dayin)
    else:
        dayin1 = dayin[0:1]
        dayin2 = dayin[1:2]
        addnum2 = int(dayin1) + int(dayin2)
    print(addnum2)
    return addnum2


def year(yearin):
    """ asks for the users birth year and adds the digits together and checks if it's a master or not.
    If not convert the input to digits and return the sum of the digits."""

    # Tests for inputs greater than or equal 13, since no months exists above 12

    if len(yearin) == 4:
        pass
    else:
        print("Error! Enter a new number:")
        yearin = (input("enter the number of your birth year:"))

    if int(yearin) % 11 == 0:
        addnum3 = 11
    else:
        yearin1 = yearin[0:1]
        yearin2 = yearin[1:2]
        yearin3 = yearin[2:3]
        yearin4 = yearin[3:4]
        addnum3 = int(yearin1) + int(yearin2) + int(yearin3) + int(yearin4)
    # Compares numbers and adds them if they are two digit. Unique case for master numbers 11, 22 and 33
    if addnum3 < 10:
        addnum4 = addnum3
    elif addnum3 % 11 == 0:
        addnum4 = addnum3
    else:
        space0 = str(addnum3)
        space1 = space0[0:1]
        space2 = space0[1:2]
        addnum4 = int(space1) + int(space2)

    if addnum4 < 10:
        addnum5 = addnum4
    elif addnum4 % 11 == 0:
        addnum5 = addnum4
    else:
        space0 = str(addnum4)
        space1 = space0[0:1]
        space2 = space0[1:2]
        addnum5 = int(space1) + int(space2)
    print(addnum5)

    return addnum5


def calculate(life):
    if life < 10:
        life2 = life
    elif life % 11 == 0:
        life2 = life
    else:
        path1 = str(life)
        path2 = path1[0:1]
        path3 = path1[1:2]
        life2 = int(path2) + int(path3)

    if life2 < 10:
        life_path_num = life2
    elif life2 % 11 == 0:
        life_path_num = life2
    else:
        path2 = str(life2)
        path3 = path2[0:1]
        path4 = path2[1:2]
        life_path_num = int(path3) + int(path4)
    print("Your life path number is {}".format(life_path_num))
    return life_path_num


def comments(com):
    import time
    """Provides comments to the user based on their Life Path Number"""
    if com == 1:
        print(" You must be the luckiest person on earth.")
        time.sleep(2)
        print("You have a pioneering spirit, independent nature, and innate leadership capabilities.")
    elif com == 2:
        print("Everyone wants to be like you!")
        time.sleep(2)
        print("You are incredibly sensitive, great balance, and display harmony. ")
    elif com == 3:
        print("A masterpiece of Beauty!")
        time.sleep(2)
        print("You are highly gifted at expression, seamlessly sharing innovative!")
    elif com == 4:
        print("You are highly needed for the success of this world!")
        time.sleep(2)
        print("Bravo: You are Practical, hardworking, and responsible!")
    elif com == 5:
        print("Free-thinking, adventurous, and progressive, 5 is defined by freedom!")
        time.sleep(2)
        print("What would the world be without your Stories?")
    elif com == 6:
        print("Healer!")
        time.sleep(2)
        print("Yes you are! 6 is recognized for its nurturing, supportive, and empathic nature.")
    elif com == 7:
        print("You Love mystery! Adventure, Great with numbers")
        time.sleep(2)
        print("Wanna be a detective?")
    elif com == 8:
        print("Abundance! Natural Born Leader")
        time.sleep(2)
        print("Ambitious and goal-oriented,")
    elif com == 9:
        print("You are no stranger life’s ups-and-downs of life — been there, done that.")
        time.sleep(2)
        print("Experience is indeed the best teacher")
    elif com == 11:
        print("You're a Master Decent")
        time.sleep(2)
        print("You are filled with lots of energy. A healer of oneself!")
    elif com == 22:
        print("You are a master builder")
        time.sleep(2)
        print("What would the world be without your Stories?")
    elif com == 33:
        print("You are very knowledgeable")
        time.sleep(2)
        print("The wisest of them all!")
    else:
        print("Sorry your number doesn't exist, a unique being indeed!")


def main():
    """call all the previously defined functions to the main.
    Collects input statements from the user and passes its parameter to the functions. """
    first_val = (input("Howdy, Please enter your birth month. For example, July would be 7:"))
    monthnum = month(first_val)
    second_val = (input("One step closer. Now enter the number of your birth day:"))
    daynum = day(second_val)
    third_val = (input("Please enter the number of your birth year:"))
    yearnum = year(third_val)
    life1 = monthnum + daynum + yearnum
    number = calculate(life1)
    comments(number)

# Bravo! The End
main()

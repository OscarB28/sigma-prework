# get required packages
import datetime


def date_to_age(dob):
    # get date using .today() method
    date_today = datetime.date.today()
    # convert date today and date given into timedelta codes
    date_code = datetime.datetime.strptime(
        str(date_today), "%Y-%m-%d")
    dob_code = datetime.datetime.strptime(str(dob), "%Y-%m-%d")
    # take away from each other to get amount of days (need to divide so that there is no hours minutes seconds included)
    days_between = (date_code - dob_code)/datetime.timedelta(days=1)
    # divide by days in a year including leap years and return
    age = int(days_between/365.25)
    return age


def main():
    date = input(
        "What is the date you would like to find out an age from? (yyyy-mm-dd format)\n")
    age = date_to_age(date)
    print("This person is {} years old.".format(age))


main()

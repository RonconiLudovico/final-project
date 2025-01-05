# Here the function to add one or more seats will be implemented

from utils.assign_var import *

# In the following function I tried to write a function that prompts the user for how many seats to add and updates them
# ! ! ! ! PROBLEM: When running the code, after placing a reservation, if we get to the manage menu (manage_res.py) and try loading the add function,
#                  The program will load the main "reservation function" (navigate funct in decision_making.py)
def add_seat(Id):
    seatsToAdd = ask_how_many_seats()
    update_reservation(reservationDict, Id, seatsToAdd)
    print(f"You added {seatsToAdd} seats successfully!\n")


def ask_how_many_seats():
    return int(input("How many seats would you like to add? \n"))


def update_reservation(reservationDict, Id, seatsToAdd):
    reservationDict[Id][1] = seatsToAdd + int(reservationDict[Id][1])
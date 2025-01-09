# Here the function to add one or more seats will be implemented

from utils.assign_var import movieSchedule, reservationDict, seats, movieList
from utils.go_back import go_back

# In the following function I tried to write a function that prompts the user for how many seats to add and updates them

def add_seat(Id):
    seatsToAdd = ask_how_many_seats(Id)
    update_reservation(reservationDict, Id, seatsToAdd)
    print(f"You added {seatsToAdd} seats successfully!\n")
    go_back()


def ask_how_many_seats(moviesId):
    seatsAsked = int(input("How many seats would you like to add? \n"))

    if seatsAsked == 0:
        print("You have to add at least 1 seat! \n\n")
        ask_how_many_seats()
    
    elif seatsAsked < 0:
        print("You can't add a negative number of seats! \n\n")
        ask_how_many_seats()
    
    elif seatsAsked > movieList[reservationDict[moviesId][0]][seats]:
        print("There are not enough seats for the chosen show! \n\n")
        ask_how_many_seats(moviesId)
    
    else:
        return seatsAsked


def update_reservation(reservationDict, Id, seatsToAdd):
    reservationDict[Id][1] += seatsToAdd
    movieSchedule[reservationDict[Id][0]][seats] -= seatsToAdd
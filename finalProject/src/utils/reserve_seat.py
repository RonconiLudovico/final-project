# The following program creates a reservation
# It starts by importing all the needed variables and the randint module from random
from time import sleep
from utils.assign_var import *
from random import randint

# The following fucntion displays the screenings schedule
def screenings():
    header = "{:<30} {:<30} {:30}".format(Id , title, time)
    program = []

    for movie in movieList:
        rowMovie = "{:<30} {:<30} {:<30}".format(movie[Id], movie[title], movie[time])
        program.append(rowMovie)

    print(f"{header.upper()}\n\n{"\n\n".join(program)}\n")

# The following function starts by calling first the previous function, then asks the user for the movie to reserve and finally calls the
# select_seats function with the movie Id as argument
def choose_movie():
    screenings()

    movieChoice = int(input("\nFor which projection would you like to book some seats? [Enter Id]\n"))

    if movieChoice > 5:
        print("PLEASE INPUT A VALID MOVIE ID! \n\n")
        sleep(0.5)
        choose_movie()
    print(select_seats(movieChoice))

# The following function starts by asking how many seats would the user like to book, then it updates the number of available seats subtracting the n of seats booked
# then it passes in the empty dict reservationDict a new element with the reservation infos as value under the form of a tuple, passing a random integer as the key which will
# represent the reservation id
# finally it prints out the reservation details
def select_seats(movieId):
    seatsToBeBooked = input("\nHow many seats would you like to book? ")

    movieSchedule[movieId - 1][seats] -= int(seatsToBeBooked)

    reservationDict[randint(00000, 99999)] =[movieId, seatsToBeBooked]

    return f"\nReservation number: {list(reservationDict)[-1]}\n\nyou have booked {seatsToBeBooked} seats for the movie {movieSchedule[movieId - 1][title]}\n"

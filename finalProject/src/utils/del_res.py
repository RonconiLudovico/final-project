# Here I implemented a program which deletes a reservation and updates the reservation dictionary and the movie schedule

from utils.assign_var import reservationDict, movieSchedule, seats
from utils.go_back import go_back

def delete_res(Id):
    confirm = input("Are you sure you want to delete this reservation? [Y/N] \n")

    if confirm.lower() == "y":
        print(f"Reservation {Id} has been deleted\n")
        movieSchedule[reservationDict[Id][0]][seats] += reservationDict[Id][1]
        del reservationDict[Id]
        go_back()
        
    else:
        print("Reservation not deleted\n")
        go_back()
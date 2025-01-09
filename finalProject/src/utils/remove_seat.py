from utils.assign_var import reservationDict, movieSchedule, seats
from utils.go_back import go_back

def update_reservation_remove(reservationDict, Id, seatsToRemove):
    reservationDict[Id][1] -= seatsToRemove
    movieSchedule[reservationDict[Id][0]][seats] += seatsToRemove


def ask_seats_to_remove():
    seatsAsked = int(input("How many seats would you like to remove? \n"))

    if seatsAsked == 0:
        print("You have to remove at least 1 seat! \n\n")
        ask_seats_to_remove()
    
    elif seatsAsked < 0:
        print("You can't remove a negative number of seats! \n\n")
        ask_seats_to_remove()
    
    else:
        return seatsAsked
    

def remove_seat(Id):
    seatsToRemove = ask_seats_to_remove()
    update_reservation_remove(reservationDict, Id, seatsToRemove)
    print(f"You removed {seatsToRemove} seats successfully!\n")
    go_back()
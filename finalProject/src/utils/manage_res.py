# The following file starts by importing all the needed variables and the function that create the managing system

from utils.assign_var import *
from utils.add_seat import add_seat
from utils.remove_seat import remove_seat
from utils.del_res import delete_res
from utils.go_back import go_back


# The program starts here by prompting the user for a reservation number, calling then the reservation
def manage():
    reservationId = int(input("\n\nPlease insert your reservation number: ---- Go Back[0]\n\n"))
    if reservationId == 0:
        go_back()
    
    open_reservation(reservationId)

# Here a dictionary is defined in which different functions are called depending on what the user prompted
managing_actions = {
    "1" : add_seat,
    "2" : remove_seat,
    "3" : delete_res,
}
# Then the reservation is opened and the details are shown, the user can choose what to do with the reservation,
# if the reservation number is not found the programm will say so to the user and ask for the reservation number again
def open_reservation(Id):

    if Id in reservationDict.keys():
        print(f"\nYour reserved {reservationDict[Id][1]} seat(s) for the show {movieSchedule[reservationDict[Id][0] - 1][title]}\n\nwhat would you like to do?\n")
        navigate_managing(Id)

    elif Id == 9:
        exit
    
    elif Id == 0:
        pass

    else:
        print("Reservation number not found, please enter a valid reservation number\n")
        manage()

# the following function calls the function corresponding to the choice made
def navigate_managing(Id):
    print(menus["3"])
    choice = input("Please choose an action: ")

    if choice in managing_actions:
        managing_actions[choice](Id)

    elif choice == 0:
        go_back()
  
    else:
        print("invalid choice please try again.\n")
        navigate_managing(Id)

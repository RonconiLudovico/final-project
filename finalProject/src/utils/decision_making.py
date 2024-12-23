# Here after defining the different menus as a dict and the related actions as anopther dict,
# I created a function in which depending on the input passed as arguments will run the relative function

from utils.view_infos import show_infos
from utils.reserve_seat import choose_movie
from utils.manage_res import manage

menus = {
    "0" : "Make Reservation [1] ---- Check Availability [2] ---- Manage Reservation [3] ---- Exit [9]\n",
    "1" : "\nGo Back [0]\n",
    "2" : "\nGo Back [0]\n",
    "3" : "Add a seat [1] ---- Move a seat [2] ---- Remove a seat [3] ---- Go Back [0]\n",
    "9" : "Thank you for using our Cinema booking Manager :)"
    }

actions = {
    "1" : choose_movie,
    "2" : show_infos,
    "3" : manage
}

def navigate(choice):
    if choice in actions:
        actions[choice]()
        
    if choice in menus:
        print(menus[choice])

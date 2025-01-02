# Here after defining the different menus as a dict and the related actions as anopther dict,
# I created a function in which depending on the input passed as arguments will run the relative function

from utils.view_infos import show_infos
from utils.reserve_seat import choose_movie
from utils.manage_res import manage
from utils.assign_var import menus

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

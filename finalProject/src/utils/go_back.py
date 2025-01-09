# Here I implemented a program which is used to go back to the main menu,
# it also prints the main menu because with the previous implementation there would have been duplicates

from utils.assign_var import menus

def go_back():
    print(menus["0"])
    return
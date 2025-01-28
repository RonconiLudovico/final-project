import sys

from utils.convert_json import menu
from utils.show_objects import show_objects
from utils.ask_obj_info import ask_object_info_to_add, ask_object_info_to_else
from utils.add_object import add_object
from utils.delete_object import del_object
from utils.edit_object import edit_object

def check_exit(choice): # Here we check for the "0" choice meaning the user wants to exit
    if choice == "0":
        sys.exit()



def menu_engine():
    while True:   # We start a while True loop
        print(menu["main"])   # We output the menu
        choice = input("What would you like to do?\n")
        check_exit(choice)

        if choice == "1":
            print(f"\n\n{show_objects()}\n")

        elif choice == "2":
            print(f"\n{menu["add"]}\n")
            add_object(ask_object_info_to_add())

        elif choice == "3":
            print(f"\n{menu["remove"]}\n")
            del_object(ask_object_info_to_else())
        
        elif choice == "4":
            print(f"\n{menu["edit"]}\n")
            edit_object(ask_object_info_to_else())
        
        else:
            break




if __name__ == "__main__":
    menu_engine()
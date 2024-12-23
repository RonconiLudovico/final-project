# This is the main program so far, will be implemented in the future
# First it imports the loading function and everything from the decision_making file

from utils import loading
from utils.decision_making import *

# Here I defined a function that prompts the user for a choice
def get_choice():
    return input("What would you like to do? ")

# The main program will keep on running to navigate through the different parts of the program, if 9 is prompted the program will stop
def main():
    while True:
        choice = get_choice()
        navigate(choice)
        
        if choice == "9":
            break



# Here first the loading gets called, then the basic manu is printed and finally the main function is called to actually start the program
if __name__ == "__main__":
    loading
    print(menus["0"])
    main()

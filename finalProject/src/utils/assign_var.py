# In the following file I extracted the single datas from the JSON file and associated each one to a variable
# to later use in other scripts in a much cleaner form

import json

screeeningInfos = open('/home/ronco_ubuntu/python_projects/final-project/finalProject/docs/screening_infos.json')

data = json.load(screeeningInfos)

movieSchedule = data["screenings"]

movieList = [
    movieSchedule[0],
    movieSchedule[1],
    movieSchedule[2],
    movieSchedule[3],
    movieSchedule[4]
    ]

title = "movieTitle"

time = "timeScheduled"

theater = "theater"

seats = "availableSeats"

Id = "Id"

# The following is an empty dict in which the program will store the reservations once made

reservationDict = {}

# The following is a dictionary with all the text for the menu
menus = {
    "0" : "Make Reservation [1] ---- Check Availability [2] ---- Manage Reservation [3] ---- Exit [9]\n",
    "1" : "\nGo Back [0] ---- Exit [9]\n",
    "2" : "\nGo Back [0] ---- Exit [9]\n",
    "3" : "Add a seat [1] ---- Move a seat [2] ---- Remove a seat [3] ---- Go Back [0] ---- Exit [9]\n",
    "9" : "Thank you for using our Cinema booking Manager :)"
    }
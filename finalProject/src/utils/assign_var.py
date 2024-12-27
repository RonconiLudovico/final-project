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

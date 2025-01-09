# Here I created a function which will return the infos for all the screenings as a Table

from utils.assign_var import movieList, menus, title, time, theater, seats

def show_infos():
    header = "{:<30} {:<30} {:30} {:<30}".format(title, time, theater, seats)
    program = []

    for movie in movieList:
        rowMovie = "{:<30} {:<30} {:30} {:<30}".format(movie[title], movie[time], movie[theater], movie[seats])
        program.append(rowMovie)

    print(f"{header.upper()}\n\n{"\n\n".join(program)}\n\n")
    print(menus["2"])

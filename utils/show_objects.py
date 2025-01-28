from utils.convert_json import locations

def show_objects():
    '''
    Here we'll start by assigning to variables the list of keys and values of the locations dict
    Then we'll return the result of the recursive function
    '''
    rooms = list(locations.keys())
    items = list(locations.values())

    return recursive(rooms, items) 


def recursive(rooms, items):
    '''
    Here we will implement the function show_objects to recursively return a string of all the objects
    '''
    
    if not items[0]:  # If no values are found for the items in the room than nothing should be added to the string
        return ""
    
    else:   # Otherwise we should add a formatted string for each first value, 
        return f"{rooms[0]} contains: {", ".join(items[0])};\n{recursive(rooms[1:], items[1:])}"
            # followed by the recursion with the arguments stripped of the first value
    
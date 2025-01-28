from utils.convert_json import locations, objects

def edit_object(obj):
    '''
    This function edits an object in a destination dictionary
    '''
    edit_choice = input("What would you like to edit? (name, location, category) ")

    if edit_choice == "name":
        edit_name(obj)

    elif edit_choice == "location":
        edit_location(obj)

    else:
        edit_category(obj)

    print("The object has been successfully edited!\n")


def edit_name(obj):
    '''
    This function edits the name of an object in the registry
    '''
    locations[obj[1]].remove(obj[0])
    obj[0] = input("What is the new object's name? ")
    objects[obj[0]] = obj[1:]
    locations[obj[1]].append(obj[0])


def edit_location(obj):
    '''
    This function edits the location of the specified object
    '''
    obj[1] = input("What is the new object's location? ")
    objects[obj[0]] = obj[1:]
    locations[obj[1]].append(obj[0])


def edit_category(obj):
    '''
    This function edits the category of the specified object
    '''
    obj[2] = input("What is the new object's category? ")
    objects[obj[0]] = obj[1:]
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


def edit_name(obj):
    '''
    This function edits the name of an object in the registry
    '''
    locations[obj['location']].remove(obj['name'])
    obj['name'] = input("What is the new object's name? ")
    objects.append(obj)
    locations[obj['location']].append(obj['name'])


def edit_location(obj):
    '''
    This function edits the location of the specified object
    '''
    locations[obj['location']].remove(obj['name'])
    obj['location'] = input("What is the new object's location? ")
    objects.append(obj)
    locations[obj['location']].append(obj['name'])

def edit_category(obj):
    '''
    This function edits the category of the specified object
    '''
    obj['category'] = input("What is the new object's category? ")
    objects.append(obj)
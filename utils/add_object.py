from utils.convert_json import objects, locations

def add_object(obj):
    '''
    This function adds an object to a destination dictionary
    '''
    locations[obj['location']].append(obj['name'])
    objects.append(obj)
    print(f"obj{'name'} has been added to the registry!\n")
    return
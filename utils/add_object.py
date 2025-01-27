from utils.convert_json import objects, locations

def add_object(obj):
    '''
    This function adds an object to a destination dictionary
    '''
    locations[obj[1]].append(obj[0])
    objects[obj[0]] = list([obj[1], obj[2]])
    print(f"obj{'name'} has been added to the registry!\n{objects}")
    return
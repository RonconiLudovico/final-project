from utils.convert_json import objects, locations

def del_object(obj):
    '''
    This function deletes the provided object from the registry
    '''
    
    if obj[0] in locations[obj[1]] and obj[1] in locations.keys():
        locations[obj[1]].remove(obj[0])

    if obj[0] in objects.keys():
        del objects[obj[0]]
    else:
        return
    
    print(f"Object deleted successfully\n{objects}\n{locations}")
    return
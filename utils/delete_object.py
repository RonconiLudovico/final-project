from utils.convert_json import objects, locations

def del_object(obj):
    '''
    This function deletes the provided object from the registry
    '''
    if obj in objects:
        objects.remove(obj)
    else:
        print("Object not found in the registry")
        return
    
    locations[obj['location']].remove(obj['name'])
    print("Object deleted successfully")
    return
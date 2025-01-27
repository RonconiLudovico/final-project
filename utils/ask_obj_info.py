from utils.convert_json import objects, locations, menu

def ask_object_info():
    '''
    This function asks the user for the object's information
    '''
    object_name = input("What is the object's name? ")
    object_location = input("Where is the object located? ")
    object_category = input("What is the object's category? ")
    return [object_name, object_location, object_category]
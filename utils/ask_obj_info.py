from utils.convert_json import objects
 

def ask_object_info_to_add():
    '''
    This function asks the user for the object's information to add a registry
    '''
    object_name = input("What is the object's name? ")
    object_location = input("Where is the object located? ")
    object_category = input("What is the object's category? ")
    return [object_name, object_location, object_category]

def ask_object_info_to_else():
    '''
    This function asks for the object name and retrieves its attributes
    '''
    object_name = input("What is the object's name? ")
    return [object_name, objects[object_name][0], objects[object_name][1]]
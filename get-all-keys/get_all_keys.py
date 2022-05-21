
def get_unique_values(array):
    """function to get unique values"""
    # initialize a null list
    print (array)
    null_list = []
    # traverse for all elements
    unique_list = [null_list.append(field) for field in array if field not in null_list] 
    
    #returns unique_list
    return null_list

def get_all_keys(*args):
    """function to get all keys"""
    my_list = [key for person in args for key in person.keys()]
    my_list = get_unique_values(my_list)
    return my_list

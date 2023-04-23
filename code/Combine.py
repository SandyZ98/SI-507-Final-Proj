
def CombineInterface(new_dict, old_dict=None):
    '''
    User could choose to save the current dictionary alone, combine it with the previous dictionary, or not save.
    Parameters:
    ----------
        new_dict (dict): the current dictionary
        old_dict (dict): the previous dictionary, defaults to None
    Returns
    -------
    A new dictionary (dict)
    
    '''
    if old_dict is None:
        print("No previous dictionary found.")
    else:
        print("Previous dictionary found.")
    print("Would you like to save the file for later?")
    print("1. Save it alone")
    print("2. Combine with the existing data")
    print("3. Do not save")
    userInput = input()
    if userInput == '1':
        return new_dict
    elif userInput == '2':
        if old_dict is None:
            print("No previous dictionary found. Cannot combine.Current one saved")
            return new_dict
        else:
            combined_dict = {**old_dict, **new_dict}
            print("Dictionaries combined.")
            return combined_dict
    elif userInput == '3':
        print("Dictionary not saved.")
        return {}
    else:
        print("Invalid input. Please input 1, 2, or 3.")
        return CombineInterface(new_dict, old_dict)


def merge_dicts(dict1, dict2 = None):
    """
    Merge two dictionaries into a single dictionary.

    Parameters:
    -----------
    dict1 : dict
        The first dictionary.
    dict2 : dict
        The second dictionary.

    Returns:
    --------
    dict : The merged dictionary.
    """
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

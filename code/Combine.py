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


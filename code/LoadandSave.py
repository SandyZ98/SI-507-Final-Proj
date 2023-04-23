import json
import os

def SaveInterface(post):
    """
    Provides a user interface for saving a given `post` object as a JSON file.

    Parameters:
        post (dict/list): The `post` object to be saved as a JSON file.

    Returns:
        None
    """
    print("Would you like to save the data as json file?: '\n' 1 = Yes; '\n' 2 = No; '\n' 3 = Quit.")
    userInput = input()
    if userInput == '1':
        filepath = input ("Please provide the file path: ")
        write_json(filepath, post)
    elif userInput == '2':
        print("Okay!")
    elif userInput == '3':
        print('\nBye Bye!\n')
        return
    else:
        print('Please input between 1, 2, 3')


def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """
    if not os.path.exists(os.path.dirname(filepath)):
        print(f"Error: {os.path.dirname(filepath)} does not exist")
        return
    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)

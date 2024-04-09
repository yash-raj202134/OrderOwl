import re

def get_str_from_food_dict(food_dict: dict):
    """
    Convert a dictionary representing food items and their quantities into a string.
    
    Parameters:
    - food_dict (dict): A dictionary where keys are food items and values are quantities.
    
    Returns:
    - result (str): A string representation of the food items and their quantities.
    """
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


def extract_session_id(session_str: str):
    """
    Extract the session ID from a given string.
    
    Parameters:
    - session_str (str): The string containing the session information.
    
    Returns:
    - extracted_string (str): The extracted session ID.
    """
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(0)
        return extracted_string

    return ""

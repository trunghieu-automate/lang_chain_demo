import json

def save_json_to_file(json_object, file_path):
    """
    Appends a JSON object to a list and saves it to a file.
    
    :param json_object: The JSON object (dictionary) to save.
    :param file_path: The path to the file where the list will be saved.
    """
    try:
        # Load existing data from the file if it exists
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []  # Initialize an empty list if the file doesn't exist or is invalid
        
        # Append the new JSON object to the list
        data.append(json_object)
        
        # Save the updated list back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        
        print("Data successfully saved to file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def load_json_file(file_path):
    """
    Appends a JSON object to a list and saves it to a file.
    
    :param json_object: The JSON object (dictionary) to save.
    """
    try:
        # Load existing data from the file if it exists
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            data = []  # Initialize an empty list if the file doesn't exist or is invalid
        
        # Append the new JSON object to the list
        return data
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

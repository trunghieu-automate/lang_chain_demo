import json
import os

def load_json_file(filepath):
    """
    Loads JSON data from a file at the given filepath.

    Args:
        filepath (str): The path to the JSON file.

    Returns:
        dict or None: The loaded JSON data as a dictionary if successful,
                       None if an error occurs.
    """
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {filepath}: {e}")
        return None
    except IOError as e:
        print(f"IOError while loading {filepath}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def save_json_file(filepath, data):
    """
    Saves the provided data to a JSON file at the given filepath.

    Args:
        filepath (str): The path to the JSON file.
        data (dict): The data to be saved as JSON.
    """
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)  # Use indent for pretty printing
        print(f"Data successfully saved to {filepath}")
    except IOError as e:
        print(f"IOError while saving to {filepath}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def delete_json_file(filepath):
    """
    Deletes the JSON file at the given filepath.

    Args:
        filepath (str): The path to the JSON file.
    """
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"File {filepath} successfully deleted.")
        else:
            print(f"File {filepath} does not exist.")
    except OSError as e:
        print(f"OSError while deleting {filepath}: {e}")


if __name__ == '__main__':
    # Example Usage:

    # Create a sample JSON file
    data = {"name": "John Doe", "age": 30, "city": "New York"}
    save_json_file("example.json", data)

    # Load the JSON file
    loaded_data = load_json_file("example.json")
    if loaded_data:
        print("Loaded data:", loaded_data)

    # Delete the JSON file
    delete_json_file("example.json")

    # Attempt to load the deleted file (demonstrates error handling)
    loaded_data = load_json_file("example.json")
    if loaded_data is None:
        print("Failed to load the deleted file.")

    # Demonstrate error handling with a non-existent file
    loaded_data = load_json_file("nonexistent.json")
    if loaded_data is None:
        print("Failed to load nonexistent.json as expected.")

    # Demonstrate deleting a file that doesn't exist
    delete_json_file("nonexistent.json")
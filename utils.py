import json
from pathlib import Path

from models import BuildingList


# Check if given file path is valid
def is_valid_file_path(path: str) -> bool:
    """
    Validate if the given string is a valid file path

    :param path: String to validate as file path
    :return: True if the path is valid and file exists, otherwise False
    """
    return Path(path).is_file()


# Load and parse the JSON data file
def load_data(filepath: str) -> BuildingList:
    """
    Load Building data from json file and validate as per Building Model

    :param filepath: path to load data from
    :return: list of Building Model
    """
    if is_valid_file_path(filepath):
        with open(filepath, 'r') as file:
            file_data = json.load(file)
            try:
                building_data = BuildingList.model_validate(file_data)
                return building_data
            except ValueError as e:
                raise Exception(f"Failed to validate Building data with error: {e}")
    else:
        raise FileNotFoundError("File path is invalid")

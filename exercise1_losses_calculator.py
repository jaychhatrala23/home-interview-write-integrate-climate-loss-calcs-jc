import json
from pathlib import Path

import math
from typing import List

from pydantic import BaseModel, RootModel


class Building(BaseModel):
    """
    Pydantic model to validate Building Data
    """
    buildingId: int
    floor_area: int
    construction_cost: int
    hazard_probability: float
    inflation_rate: float


class BuildingList(RootModel):
    """
    Pydantic model to represent list of Building Model
    """
    root: List[Building]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


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


# Calculate total projected loss with additional complexity and errors
def calculate_projected_losses(building_data):
    total_loss = 0
    for building in building_data:
        floor_area = building['floor_area']
        construction_cost = building['construction_cost']
        hazard_probability = building['hazard_probability']
        inflation_rate = building['inflation_rate']

        # Calculate future cost
        future_cost = construction_cost * (1 + inflation_rate)  

        # Calculate risk-adjusted loss
        risk_adjusted_loss = future_cost * (1 - hazard_probability) 

        # Calculate present value of the risk-adjusted loss
        discount_rate = 0.05  # Assuming a 5% discount rate
        present_value_loss = risk_adjusted_loss / (1 + discount_rate)

        # Calculate maintenance and total maintenance cost
        maintenance_cost = floor_area * 50  # assuming a flat rate per square meter
        total_maintenance_cost = maintenance_cost / (1 + discount_rate)  

        # Total loss calculation
        total_loss += present_value_loss + total_maintenance_cost

    return total_loss


# Main execution function
def main():
    data = load_data('data.json')
    total_projected_loss = calculate_projected_losses(data)
    print(f"Total Projected Loss: ${total_projected_loss:.2f}")


if __name__ == '__main__':
    main()

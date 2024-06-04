# Scaling the Loss Calculation Model

# Laptop configuration : MacBook Pro with M1 Pro Chip ( 16 GB RAM )

# I tried to use the code from Exercise 2 and tested the time taken to calculate loss estimate
# on a dataset with data of million buildings (generated with random values). Time Taken Result - 5 seconds

# Major backlog - For Loop, due to which we face a time complexity of O(n) (linear time complexity)
# which means the time taken to execute the script is directly proportional to the length of building_data


#### SOLUTION ####

# We take a complete different approach while loading and processing data

# As we have a json file with structured data, we can represent data using Pandas
# Use vectorization techniques to implement formulas


#### Code Snippet ####


import pandas as pd

from utils import is_valid_file_path


def load_data_to_df(file_path: str) -> pd.DataFrame:
    """
    Load building data from a JSON file into a Pandas DataFrame.

    :param file_path: Path to the JSON file containing building data.
    :return: DataFrame containing the building data.
    """
    if is_valid_file_path(file_path):
        df = pd.read_json(file_path)

        # Define expected data types
        expected_dtypes = {
            'buildingId': 'int64',
            'floor_area': 'int64',
            'construction_cost': 'int64',
            'hazard_probability': 'float64',
            'inflation_rate': 'float64'
        }

        # Validate and convert data types
        for column, dtype in expected_dtypes.items():
            if column in df.columns:
                df[column] = df[column].astype(dtype)
            else:
                raise ValueError(f"Missing expected column: {column}")
        return df

    else:
        raise FileNotFoundError("File path is invalid")



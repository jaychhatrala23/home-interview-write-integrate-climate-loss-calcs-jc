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

# I used below code snippet and tested the time taken to calculate loss estimate
# on a dataset with data of million buildings (generated with random values). Time Taken Result - 1 second

# In theory, That is 1/5 th of the time taken to solve the same problem above

# If the dataset is still larger, we can use the concept of chunking in Pandas,
# which will effectively chunk the whole file into multiple parts effectively also saving the memory consumption

# Attached a file json_generator.py which was used to generate a json file with million property records


#### Code Snippet ####
import time
from math import e

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
            "buildingId": "int64",
            "floor_area": "int64",
            "construction_cost": "int64",
            "hazard_probability": "float64",
            "inflation_rate": "float64",
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


def calculate_estimated_losses_with_pandas(df: pd.DataFrame, years: int = 1) -> float:
    """
    This func will calculate the potential financial loss estimate from given Building data using Pandas

    Parameters:
    df (pd.DataFrame): DataFrame containing the building data.
    years (int): Number of years over which to calculate the losses.

    Returns:
    float: Total estimated loss.
    """

    discount_rate = 0.05  # Assuming a 5% discount rate
    denominator = (1 + discount_rate) ** years

    # Breaking the formula to make it easier to read and comprehend
    # Vectorized numerator calculation
    df["numerator"] = (
        df["construction_cost"]
        * (e ** (df["inflation_rate"] * df["floor_area"] / 1000))
        * df["hazard_probability"]
    )

    # Vectorized estimated losses calculation
    df["loss_estimate"] = df["numerator"] / denominator

    # Optional: Print estimated loss for each building
    # for _, row in df.iterrows():
    #     print(f"Estimated loss for property with id {row['buildingId']} is : ${row['loss_estimate']:.2f}")

    # Total estimated loss
    total_loss_estimate = df["loss_estimate"].sum()

    return total_loss_estimate


# Main execution function
def main():
    start_time = time.time()
    # using dataset with million properties
    data = load_data_to_df("data_million.json")
    total_loss_estimate = calculate_estimated_losses_with_pandas(data)
    print(f"Total Estimated Loss for all properties : ${total_loss_estimate:.2f}")
    elapsed_time = time.time() - start_time
    print("Elapsed time : ", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


if __name__ == "__main__":
    main()

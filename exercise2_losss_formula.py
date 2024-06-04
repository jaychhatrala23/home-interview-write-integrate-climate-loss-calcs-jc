from math import e
from models import Building
from utils import load_data


def calculate_estimated_losses(building_data: [Building], years: int = 1) -> float:
    """
    This func will calculate the potential financial loss estimate from given Building data

    :param building_data: list of Building Model
    :param years: Number of years to consider for calculating projected losses, defaults to 1
    :return: Total potential financial loss estimate of all properties
    """
    total_loss_estimate = 0

    for building in building_data:
        building_id = building.buildingId
        floor_area = building.floor_area
        construction_cost = building.construction_cost
        hazard_probability = building.hazard_probability
        inflation_rate = building.inflation_rate
        discount_rate = 0.05  # Assuming a 5% discount rate

        # Breaking the formula to make it easier to read and comprehend
        numerator = construction_cost * (e ** (inflation_rate * floor_area / 1000)) * hazard_probability
        denominator = (1 + discount_rate) ** years

        loss_estimate = numerator / denominator

        print(f"Estimated loss for property with id {building_id} is : ${loss_estimate:.2f}")

        total_loss_estimate += loss_estimate

    return total_loss_estimate


# Main execution function
def main():
    data = load_data('data.json')
    total_estimated_loss = calculate_estimated_losses(data)
    print(f"Total Estimated Loss for all properties : ${total_estimated_loss:.2f}")


if __name__ == '__main__':
    main()

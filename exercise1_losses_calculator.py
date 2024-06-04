from models import Building
from utils import load_data


# Calculate total projected loss with additional complexity and errors
def calculate_projected_losses(building_data: [Building], years: int = 1) -> float:
    """
    This function will calculate the total projected loss for the given building data and number of years

    :param building_data: list of Building Model
    :param years: Number of years to consider for calculating projected losses, defaults to 1
    :return: Total projected losses for all buildings
    """
    total_loss = 0
    for building in building_data:
        # Using Pydantic model fields instead of dict keys will reduce any typo errors making it more explicit
        floor_area = building.floor_area
        construction_cost = building.construction_cost
        hazard_probability = building.hazard_probability
        inflation_rate = building.inflation_rate

        # Calculate future cost
        # Updating formula to consider inflation over specified number of years
        future_cost = construction_cost * ((1 + inflation_rate) ** years)

        # Calculate risk-adjusted loss
        # Updating formula to match the description of calculating Risk-Adjusted Loss Calculation
        risk_adjusted_loss = future_cost * hazard_probability

        # Calculate present value of the risk-adjusted loss
        discount_rate = 0.05  # Assuming a 5% discount rate
        # updated formula to consider specified number of years
        present_value_loss = risk_adjusted_loss / ((1 + discount_rate) ** years)

        # Calculate maintenance and total maintenance
        # This block is irrelevant as there are no mentions of maintenance cost to consider in given description
        # maintenance_cost = floor_area * 50  # assuming a flat rate per square meter
        # total_maintenance_cost = maintenance_cost / (1 + discount_rate)

        # Total loss calculation
        total_loss += present_value_loss

    return total_loss


# Main execution function
def main():
    data = load_data('data.json')
    total_projected_loss = calculate_projected_losses(data)
    # Example, To calculate total_project_loss for 3 years :
    # total_projected_loss = calculate_projected_losses(data, years=3)
    print(f"Total Projected Loss: ${total_projected_loss:.2f}")


if __name__ == '__main__':
    main()

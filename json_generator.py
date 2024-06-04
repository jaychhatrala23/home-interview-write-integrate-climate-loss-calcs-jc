import json
import random

# Run this file to generate a json file with million property records with scrambled values
# This script is made just to create a json file with more data, this script is not optimized
# and might take a 2/3 seconds to generate the required file.

if __name__ == '__main__':
    data = [{
        "buildingId": i,
        "floor_area": random.randrange(1, 30) * 100,
        "construction_cost": random.randrange(10, 30) * 100,
        "hazard_probability": random.choice([0.1, 0.2, 0.3, 0.4, 0.5]),
        "inflation_rate": random.choice([0.1, 0.2, 0.3, 0.4, 0.5]),
    } for i in range(1, 1000001)]

    with open('data_million.json', 'w') as fp:
        json.dump(data, fp)

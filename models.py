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

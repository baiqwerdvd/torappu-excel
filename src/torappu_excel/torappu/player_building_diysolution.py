from .player_building_furniture_position_info import PlayerBuildingFurniturePositionInfo
from ..common import BaseStruct


class PlayerBuildingDIYSolution(BaseStruct):
    wallPaper: str | None
    floor: str | None
    carpet: list[PlayerBuildingFurniturePositionInfo]
    other: list[PlayerBuildingFurniturePositionInfo]

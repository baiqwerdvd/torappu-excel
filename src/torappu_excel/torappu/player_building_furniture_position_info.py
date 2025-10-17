from .player_building_grid_position import PlayerBuildingGridPosition
from ..common import BaseStruct


class PlayerBuildingFurniturePositionInfo(BaseStruct):
    id: str
    coordinate: PlayerBuildingGridPosition

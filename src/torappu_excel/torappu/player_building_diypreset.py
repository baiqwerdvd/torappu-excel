from .player_building_diysolution import PlayerBuildingDIYSolution
from ..common import BaseStruct


class PlayerBuildingDIYPreset(BaseStruct):
    name: str
    roomType: str
    solution: PlayerBuildingDIYSolution
    thumbnail: str

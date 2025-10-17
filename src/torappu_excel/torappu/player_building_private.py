from .player_building_diysolution import PlayerBuildingDIYSolution
from ..common import BaseStruct


class PlayerBuildingPrivate(BaseStruct):
    owners: list[int]
    comfort: int
    diySolution: PlayerBuildingDIYSolution

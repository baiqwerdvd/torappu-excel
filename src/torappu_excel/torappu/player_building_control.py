from .player_building_control_buff import PlayerBuildingControlBuff
from ..common import BaseStruct


class PlayerBuildingControl(BaseStruct):
    buff: PlayerBuildingControlBuff
    apCost: int
    lastUpdateTime: int
    presetQueue: list[list[int]]

from .player_building_power_buff import PlayerBuildingPowerBuff
from ..common import BaseStruct


class PlayerBuildingPower(BaseStruct):
    buff: PlayerBuildingPowerBuff
    presetQueue: list[list[int]]

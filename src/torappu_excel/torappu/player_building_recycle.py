from typing import Any

from .building_buff_display import BuildingBuffDisplay
from .player_building_recycle_buff import PlayerBuildingRecycleBuff
from .player_room_state import PlayerRoomState
from ..common import BaseStruct


class PlayerBuildingRecycle(BaseStruct):
    boostRemainTime: int
    buff: PlayerBuildingRecycleBuff
    capacity: int
    completeWorkTime: int
    curPoint: float | int
    display: BuildingBuffDisplay
    lastUpdateTime: int
    poolId: str
    presetQueue: list[list[int]]
    productList: list[Any]
    speed: float | int
    state: PlayerRoomState
    totalPoint: int

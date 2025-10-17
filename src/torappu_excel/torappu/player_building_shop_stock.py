from .date_time import DateTime
from .player_room_state import PlayerRoomState
from ..common import BaseStruct


class PlayerBuildingShopStock(BaseStruct):
    buffSpeed: float
    state: PlayerRoomState
    formulaId: str
    itemCnt: int
    processPoint: float
    lastUpdateTime: DateTime
    saveTime: int
    completeWorkTime: DateTime

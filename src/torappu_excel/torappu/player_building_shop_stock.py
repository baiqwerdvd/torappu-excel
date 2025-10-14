from pydantic import BaseModel, ConfigDict

from .date_time import DateTime
from .player_room_state import PlayerRoomState


class PlayerBuildingShopStock(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buffSpeed: float
    state: PlayerRoomState
    formulaId: str
    itemCnt: int
    processPoint: float
    lastUpdateTime: DateTime
    saveTime: int
    completeWorkTime: DateTime

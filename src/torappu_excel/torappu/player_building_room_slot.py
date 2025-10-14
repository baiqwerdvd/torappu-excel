from pydantic import BaseModel, ConfigDict

from .building_data import BuildingData
from .player_room_slot_state import PlayerRoomSlotState


class PlayerBuildingRoomSlot(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    level: int
    state: PlayerRoomSlotState
    roomId: "BuildingData.RoomType"
    charInstIds: list[int]
    completeConstructTime: int

from .building_data import BuildingData
from .player_room_slot_state import PlayerRoomSlotState
from ..common import BaseStruct


class PlayerBuildingRoomSlot(BaseStruct):
    level: int
    state: PlayerRoomSlotState
    roomId: "BuildingData.RoomType"
    charInstIds: list[int]
    completeConstructTime: int

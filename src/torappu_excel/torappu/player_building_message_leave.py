from .player_building_message_leave_sp import PlayerBuildingMessageLeaveSP
from ..common import BaseStruct


class PlayerBuildingMessageLeave(BaseStruct):
    inUse: bool
    lastVisitTs: int
    lastShowTs: int
    lastUpdateSpTs: int
    sp: PlayerBuildingMessageLeaveSP

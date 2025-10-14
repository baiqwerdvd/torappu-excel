from pydantic import BaseModel, ConfigDict

from .player_building_message_leave_sp import PlayerBuildingMessageLeaveSP


class PlayerBuildingMessageLeave(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    inUse: bool
    lastVisitTs: int
    lastShowTs: int
    lastUpdateSpTs: int
    sp: PlayerBuildingMessageLeaveSP

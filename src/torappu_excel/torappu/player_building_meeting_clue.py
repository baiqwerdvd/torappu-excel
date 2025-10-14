from pydantic import BaseModel, ConfigDict

from .player_building_meeting_clue_char import PlayerBuildingMeetingClueChar


class PlayerBuildingMeetingClue(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: str
    number: int
    uid: int
    nickNum: str
    name: str
    chars: list[PlayerBuildingMeetingClueChar]
    inUse: int
    ts: int | None = None

from .player_building_meeting_clue_char import PlayerBuildingMeetingClueChar
from ..common import BaseStruct


class PlayerBuildingMeetingClue(BaseStruct):
    id: str
    type: str
    number: int
    uid: str
    nickNum: str
    name: str
    chars: list[PlayerBuildingMeetingClueChar]
    inUse: int
    ts: int | None = None

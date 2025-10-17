from .player_building_char_bubble import PlayerBuildingCharBubble
from ..common import BaseStruct


class PlayerBuildingChar(BaseStruct):
    charId: str
    lastApAddTime: int
    ap: int
    roomSlotId: str
    index: int
    changeScale: int
    bubble: "PlayerBuildingChar.BubbleContainer"
    workTime: int
    privateRooms: list[str]
    skin: str | None = None

    class BubbleContainer(BaseStruct):
        normal: PlayerBuildingCharBubble
        assist: PlayerBuildingCharBubble
        private: PlayerBuildingCharBubble

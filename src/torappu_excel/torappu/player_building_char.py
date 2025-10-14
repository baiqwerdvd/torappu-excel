from pydantic import BaseModel, ConfigDict

from .player_building_char_bubble import PlayerBuildingCharBubble


class PlayerBuildingChar(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
    lastApAddTime: int
    ap: int
    roomSlotId: str
    index: int
    changeScale: int
    bubble: "PlayerBuildingChar.BubbleContainer"
    workTime: int
    skin: str | None = None
    privateRooms: list[str]

    class BubbleContainer(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        normal: PlayerBuildingCharBubble
        assist: PlayerBuildingCharBubble
        private: PlayerBuildingCharBubble

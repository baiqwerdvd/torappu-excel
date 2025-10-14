from pydantic import BaseModel, ConfigDict

from .player_roguelike_node import PlayerRoguelikeNode


class PlayerRoguelikeZone(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneId: str
    nodes: dict[int, PlayerRoguelikeNode]

from pydantic import BaseModel, ConfigDict

from .player_roguelike_node import PlayerRoguelikeNode
from .player_roguelike_zone_type import PlayerRoguelikeZoneType


class PlayerRoguelikeV2Zone(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    nodes: dict[int, PlayerRoguelikeNode]
    variation: list[str]
    type: PlayerRoguelikeZoneType

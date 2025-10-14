from pydantic import BaseModel, ConfigDict

from .player_roguelike_state import PlayerRoguelikeState
from .roguelike_node_position import RoguelikeNodePosition


class PlayerRoguelikeCursor(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneIndex: int
    position: RoguelikeNodePosition
    state: PlayerRoguelikeState

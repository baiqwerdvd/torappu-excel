from pydantic import BaseModel, ConfigDict

from .player_roguelike_zone import PlayerRoguelikeZone


class PlayerRoguelikeDungeon(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zones: dict[int, PlayerRoguelikeZone]

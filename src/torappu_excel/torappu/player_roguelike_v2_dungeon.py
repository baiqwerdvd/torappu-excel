from pydantic import BaseModel, ConfigDict

from .player_roguelike_v2_zone import PlayerRoguelikeV2Zone


class PlayerRoguelikeV2Dungeon(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zones: dict[int, PlayerRoguelikeV2Zone]
    verticalCostDelta: int | None = None

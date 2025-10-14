from pydantic import BaseModel, ConfigDict

from .player_home_condition_progress import PlayerHomeConditionProgress


class PlayerHomeUnlockStatus(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unlock: int | None = None
    conditions: dict[str, PlayerHomeConditionProgress] | None = None

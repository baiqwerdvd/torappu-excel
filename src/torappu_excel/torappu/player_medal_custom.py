from pydantic import BaseModel, ConfigDict

from .player_medal_custom_layout import PlayerMedalCustomLayout


class PlayerMedalCustom(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    currentIndex: str
    customs: dict[str, PlayerMedalCustomLayout]

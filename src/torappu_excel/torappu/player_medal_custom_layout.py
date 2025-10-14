from pydantic import BaseModel, ConfigDict

from .player_medal_custom_layout_item import PlayerMedalCustomLayoutItem


class PlayerMedalCustomLayout(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    layout: list[PlayerMedalCustomLayoutItem]

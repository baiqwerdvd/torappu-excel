from pydantic import BaseModel, ConfigDict

from .player_good_item_data import PlayerGoodItemData


class PlayerCashProgressData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    info: list[PlayerGoodItemData]

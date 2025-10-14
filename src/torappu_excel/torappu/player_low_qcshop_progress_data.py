from pydantic import BaseModel, ConfigDict

from .player_good_item_data import PlayerGoodItemData


class PlayerLowQCShopProgressData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    curGroupId: str
    curShopId: str
    info: list[PlayerGoodItemData]

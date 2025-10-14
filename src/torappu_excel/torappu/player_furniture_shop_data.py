from pydantic import BaseModel, ConfigDict

from .player_good_item_data import PlayerGoodItemData


class PlayerFurnitureShopData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    info: list[PlayerGoodItemData]
    groupInfo: dict[str, int]

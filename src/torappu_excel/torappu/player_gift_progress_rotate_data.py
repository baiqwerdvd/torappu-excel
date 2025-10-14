from pydantic import BaseModel, ConfigDict

from .player_good_item_data import PlayerGoodItemData


class PlayerGiftProgressRotateData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    curGroupId: str
    info: list[PlayerGoodItemData]

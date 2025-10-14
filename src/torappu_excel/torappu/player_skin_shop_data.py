from pydantic import BaseModel, ConfigDict

from .player_blindbox_data import PlayerBlindboxData
from .player_good_item_data import PlayerGoodItemData


class PlayerSkinShopData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    info: list[PlayerGoodItemData] | None = None
    gachaGood: PlayerBlindboxData

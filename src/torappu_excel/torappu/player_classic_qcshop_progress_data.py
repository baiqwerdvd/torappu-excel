from pydantic import BaseModel, ConfigDict

from .player_good_item_data import PlayerGoodItemData
from .player_good_progress_data import PlayerGoodProgressData


class PlayerClassicQCShopProgressData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    info: list[PlayerGoodItemData]
    progressInfo: dict[str, PlayerGoodProgressData]

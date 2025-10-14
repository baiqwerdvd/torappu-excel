from pydantic import BaseModel, ConfigDict

from .player_crisis_shop import PlayerCrisisShop
from .player_crisis_v2_season import PlayerCrisisV2Season


class PlayerCrisisV2(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    current: str
    seasons: dict[str, PlayerCrisisV2Season]
    shop: PlayerCrisisShop
    newRecordTs: int
    nst: int

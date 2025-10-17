from .player_crisis_shop import PlayerCrisisShop
from .player_crisis_v2_season import PlayerCrisisV2Season
from ..common import BaseStruct


class PlayerCrisisV2(BaseStruct):
    current: str
    seasons: dict[str, PlayerCrisisV2Season]
    shop: PlayerCrisisShop
    newRecordTs: int
    nst: int

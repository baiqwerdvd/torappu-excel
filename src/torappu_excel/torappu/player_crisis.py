from .player_crisis_season import PlayerCrisisSeason
from .player_crisis_shop import PlayerCrisisShop
from ..common import BaseStruct


class PlayerCrisisMap(BaseStruct):
    rank: int
    confirmed: int


class PlayerCrisisTrainingStage(BaseStruct):
    point: int


class PlayerCrisisTraining(BaseStruct):
    currentStage: list[str]
    stage: dict[str, PlayerCrisisTrainingStage]
    nst: int


class PlayerCrisis(BaseStruct):
    current: str
    map: dict[str, PlayerCrisisMap]
    shop: PlayerCrisisShop
    training: PlayerCrisisTraining
    season: dict[str, PlayerCrisisSeason]
    lst: int
    nst: int
    box: list["PlayerCrisis.BoxItem"]

    class BoxItem(BaseStruct):
        id: str
        type: str
        count: int

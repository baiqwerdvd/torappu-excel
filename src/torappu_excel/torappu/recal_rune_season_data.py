from .item_bundle import ItemBundle
from .recal_rune_stage_data import RecalRuneStageData
from ..common import BaseStruct


class RecalRuneSeasonData(BaseStruct):
    seasonId: str
    sortId: int
    startTs: int
    seasonCode: str
    juniorReward: ItemBundle
    seniorReward: ItemBundle
    seniorRewardHint: str
    mainMedalId: str
    picId: str
    stages: dict[str, RecalRuneStageData]

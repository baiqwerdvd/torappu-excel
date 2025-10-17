from ..common import BaseStruct


class RecalRuneConstData(BaseStruct):
    stageCountPerSeason: int
    juniorRewardMedalCount: int
    seniorRewardMedalCount: int
    unlockLevelIds: list[str]

from ..common import BaseStruct


class MissionDailyRewards(BaseStruct):
    dailyPoint: int
    weeklyPoint: int
    rewards: dict[str, dict[str, int]]

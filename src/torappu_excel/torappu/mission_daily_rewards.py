from ..common import BaseStruct


class MissionPlayerRewardGroup(BaseStruct):  # Checked
    DAILY: dict[str, int]
    WEEKLY: dict[str, int]


class MissionDailyRewards(BaseStruct):
    dailyPoint: int
    weeklyPoint: int
    rewards: MissionPlayerRewardGroup

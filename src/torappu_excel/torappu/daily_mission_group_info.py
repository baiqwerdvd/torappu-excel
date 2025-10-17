from ..common import BaseStruct


class DailyMissionGroupInfo(BaseStruct):
    startTime: int
    endTime: int
    tagState: str | None
    periodList: list["DailyMissionGroupInfo.periodInfo"]

    class periodInfo(BaseStruct):
        missionGroupId: str
        rewardGroupId: str
        period: list[int]

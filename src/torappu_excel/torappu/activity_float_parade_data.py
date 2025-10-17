from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActivityFloatParadeData(BaseStruct):
    constData: "ActivityFloatParadeData.ConstData"
    dailyDataDic: list["ActivityFloatParadeData.DailyData"]
    rewardPools: dict[str, dict[str, "ActivityFloatParadeData.RewardPool"]]
    tacticList: list["ActivityFloatParadeData.Tactic"]
    groupInfos: dict[str, "ActivityFloatParadeData.GroupData"]

    class ConstData(BaseStruct):
        cityName: str
        lowStandard: float
        variationTitle: str
        ruleDesc: str
        cityNamePic: str

    class DailyData(BaseStruct):
        dayIndex: int
        dateName: str
        placeName: str
        placeEnName: str
        placePic: str
        eventGroupId: str
        extReward: ItemBundle | None

    class RewardPool(BaseStruct):
        grpId: str
        id: str
        type: str
        name: str
        desc: str | None
        reward: ItemBundle

    class Tactic(BaseStruct):
        id: int
        name: str
        packName: str
        briefName: str
        rewardVar: dict[str, float]

    class GroupData(BaseStruct):
        groupId: str
        name: str
        startDay: int
        endDay: int
        extRewardDay: int
        extRewardCount: int

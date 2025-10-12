from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ActivityFloatParadeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    constData: "ActivityFloatParadeData.ConstData"
    dailyDataDic: list["ActivityFloatParadeData.DailyData"]
    rewardPools: dict[str, dict[str, "ActivityFloatParadeData.RewardPool"]]
    tacticList: list["ActivityFloatParadeData.Tactic"]
    groupInfos: dict[str, "ActivityFloatParadeData.GroupData"]

    class ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        cityName: str
        lowStandard: float
        variationTitle: str
        ruleDesc: str
        cityNamePic: str

    class DailyData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        dayIndex: int
        dateName: str
        placeName: str
        placeEnName: str
        placePic: str
        eventGroupId: str
        extReward: ItemBundle | None

    class RewardPool(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        grpId: str
        id: str
        type: str
        name: str
        desc: str | None
        reward: ItemBundle

    class Tactic(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: int
        name: str
        packName: str
        briefName: str
        rewardVar: dict[str, float]

    class GroupData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        groupId: str
        name: str
        startDay: int
        endDay: int
        extRewardDay: int
        extRewardCount: int

from enum import StrEnum

from .item_bundle import ItemBundle
from ..common import BaseStruct


class MiniActTrialData(BaseStruct):
    class RuleType(StrEnum):
        NONE = "NONE"
        TITLE = "TITLE"
        CONTENT = "CONTENT"

    preShowDays: int
    ruleDataList: list["MiniActTrialData.RuleData"]
    miniActTrialDataMap: dict[str, "MiniActTrialData.MiniActTrialSingleData"]

    class RuleData(BaseStruct):
        ruleType: "MiniActTrialData.RuleType"
        ruleText: str

    class MiniActTrialSingleData(BaseStruct):
        actId: str
        rewardStartTime: int
        themeColor: str
        rewardList: list["MiniActTrialData.MiniActTrialRewardData"]

    class MiniActTrialRewardData(BaseStruct):
        trialRewardId: str
        orderId: int
        actId: str
        targetStoryCount: int
        item: ItemBundle

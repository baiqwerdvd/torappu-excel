from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class MiniActTrialData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class RuleType(StrEnum):
        NONE = "NONE"
        TITLE = "TITLE"
        CONTENT = "CONTENT"

    preShowDays: int
    ruleDataList: list["MiniActTrialData.RuleData"]
    miniActTrialDataMap: dict[str, "MiniActTrialData.MiniActTrialSingleData"]

    class RuleData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        ruleType: "MiniActTrialData.RuleType"
        ruleText: str

    class MiniActTrialSingleData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        actId: str
        rewardStartTime: int
        themeColor: str
        rewardList: list["MiniActTrialData.MiniActTrialRewardData"]

    class MiniActTrialRewardData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        trialRewardId: str
        orderId: int
        actId: str
        targetStoryCount: int
        item: ItemBundle

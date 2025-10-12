from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .item_type import ItemType


class Act44SideData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneAdditionDataMap: dict[str, "Act44SideData.Act44SideZoneAdditionData"]
    customerDataMap: dict[str, "Act44SideData.Act44SideCustomerData"]
    tagDataMap: dict[str, "Act44SideData.Act44SideTagData"]
    choiceDataMap: dict[str, "Act44SideData.Act44SideChoiceData"]
    customerDialogMap: dict[str, str]
    keeperDialogMap: dict[str, str]
    newsDataMap: dict[str, "Act44SideData.Act44SideNewsData"]
    insightDescMap: dict[str, "Act44SideData.Act44SideInsightData"]
    mileStoneList: list["Act44SideData.Act44SideMileStoneData"]
    constData: "Act44SideData.Act44SideConstData"

    class Act44SideZoneAdditionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        unlockText: str

    class Act44SideCustomerData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        name: str
        imgId: str
        iconId: str
        isSp: bool
        description: str

    class Act44SideTagData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        name: str
        isSp: bool
        description: str

    class Act44SideChoiceData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        imgId: str
        attentionArrow: int
        trustArrow: int
        attentionValue: int
        trustValue: int
        patienceValue: int

    class Act44SideNewsData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        title: str
        desc1: str
        desc2: str
        imgId: str

    class InsightType(StrEnum):
        PATIENCE = "PATIENCE"
        ATTENTION = "ATTENTION"
        TRUST = "TRUST"

    class Act44SideInsightData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        type: "Act44SideData.InsightType"
        lowerDesc: str
        recommendDesc: str
        maxDesc: str

    class Act44SideMileStoneData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        mileStoneId: str
        mileStoneLvl: int
        needPointCnt: int
        rewardItem: ItemBundle

    class Act44SideMilestoneSpecialRewardInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemName: str
        point: int

    class Act44SideConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        informantUnlockStageId: str
        informantItemId: str
        informantItemType: ItemType
        informantItemCount: int
        milestoneItemId: str
        attentionMax: int
        trustMax: int
        attentionMin: int
        trustMin: int
        patienceRCRoundNum: int
        beginnerPatienceRCRoundNum: int
        specialCustomerListId: list[str]
        milestoneRewardList: list["Act44SideData.Act44SideMilestoneSpecialRewardInfo"]
        forCountBigSuccess: int
        outerOpenUnlock: str
        customerTagFormat: str

from .item_bundle import ItemBundle
from ..common import BaseStruct


class Act55SideData(BaseStruct):
    zoneAdditionDataMap: dict[str, "Act55SideData.Act55SideZoneAdditionData"]
    newspaperDataMap: dict[str, "Act55SideData.Act55SideNewspaperData"]
    fixedReportDataMap: dict[str, "Act55SideData.Act55SideFixedReportData"]
    handReportDataMap: dict[str, "Act55SideData.Act55SideHandReportData"]
    handReportColorDataMap: dict[str, "Act55SideData.Act55SideHandReportColorData"]
    reportTagList: list[str]
    battleItemLevelDataList: "list[Act55SideData.Act55SideBattleItemLevelData]"
    constData: "Act55SideData.Act55SideConstData"

    class Act55SideBattleItemLevelData(BaseStruct):
        level: int
        score: int

    class Act55SideConstData(BaseStruct):
        priceItemId: str
        priceItemType: str
        entryRequirement: str
        businessUnlockText: str
        stageUnlockText: str
        handBasicScore: int
        handPositiveScore: int
        handNegativeScore: int

    class Act55SideFixedReportData(BaseStruct):
        fixedReportId: str
        fixedReportTag: str

    class Act55SideHandReportColorData(BaseStruct):
        handReportPic_1: str
        handReportTitleColor: str
        handReportSubTitleColor: str

    class Act55SideHandReportData(BaseStruct):
        handReportId: str
        handReportPic_1: str
        handReportPic_2: str
        handReportTitleId: str
        handReportSubTitleId: str
        handReportPositiveTagList: list[str]
        handReportNegativeTagList: list[str]
        sortId: int

    class Act55SideNewspaperData(BaseStruct):
        stageId: str
        sortId: int
        stageName: str
        stageDesc: str
        bgPic: str
        unlockStageId: str
        unlockTs: int
        baseRewardList: list[ItemBundle]
        advancedRewardList: list[ItemBundle]
        basicTargetDesc: str
        advancedTargetDesc: str
        advancedTargetParam: int
        initCardIdList: list[str]
        ratingScoreList: list[int]
        maxScore: int
        picId: str
        initEmptySlot: int
        fixedReportIdList: list[str]

    class Act55SideZoneAdditionData(BaseStruct):
        zoneId: str
        unlockText: str

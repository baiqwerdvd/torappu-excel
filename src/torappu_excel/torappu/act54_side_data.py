from .item_bundle import ItemBundle
from ..common import BaseStruct


class Act54SideData(BaseStruct):
    cards: dict[str, "Act54SideData.Act54SideCardData"]
    spreads: dict[str, "Act54SideData.Act54SideSpreadData"]
    specialZoneStageInfos: list["Act54SideData.Act54SideSpecialZoneStageInfo"]
    zoneAdditionDataMap: dict[str, "Act54SideData.Act54SideZoneAdditionData"]
    constData: "Act54SideData.Act54SideConstData"

    class Act54SideCardData(BaseStruct):
        cardId: str
        sortId: int
        name: str
        charName: str
        descUpright: str
        descReverse: str
        unlockStageId: str

    class Act54SideSpreadItemInfo(BaseStruct):
        sortId: int
        name: str
        nameEnglish: str

    class Act54SideSpreadData(BaseStruct):
        spreadId: str
        sortId: int
        availTimesDivination: int
        unlockStageId: str | None
        unlockSpreadId: str | None
        spreadsToUnlock: list[str]
        name: str
        nameEnglish: str
        spreadInfoList: list["Act54SideData.Act54SideSpreadItemInfo"]
        rewards: list[ItemBundle]

    class Act54SideSpecialZoneStageInfo(BaseStruct):
        stageId: str
        sortId: int
        hasUrgentStage: bool

    class Act54SideZoneAdditionData(BaseStruct):
        zoneId: str
        unlockText: str

    class Act54SideConstData(BaseStruct):
        divinationUnlockStageId: str
        finalReward: ItemBundle
        activityItemId: str
        divinationEnterDelay: float

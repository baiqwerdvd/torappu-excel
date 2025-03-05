from .item_bundle import ItemBundle
from .rune_table import RuneTable
from ..common import BaseStruct, CustomIntEnum

from msgspec import field


class Act25SideData(BaseStruct):
    class Act25SideArchiveItemType(CustomIntEnum):
        PIC = "PIC", 0
        STORY = "STORY", 1
        BATTLE_PERFORMANCE = "BATTLE_PERFORMANCE", 2
        KEY = "KEY", 3
        ENUM = "ENUM", 4

    class Act25SideArchiveItemUnlockType(CustomIntEnum):
        MISSION = "MISSION", 0
        STAGE = "STAGE", 1
        BUFF = "BUFF", 2

    class Act25sideTechType(CustomIntEnum):
        TECH_1 = "TECH_1", 0
        TECH_2 = "TECH_2", 1
        TECH_3 = "TECH_3", 2
        TECH_4 = "TECH_4", 3
        TECH_NUM = "TECH_NUM", 4

    tokenItemId: str
    constData: "Act25SideData.ConstData"
    zoneDescList: dict[str, "Act25SideData.ZoneDescInfo"]
    archiveItemData: dict[str, "Act25SideData.ArchiveItemData"]
    arcMapInfoData: dict[str, "Act25SideData.ArchiveMapInfoData"]
    areaInfoData: dict[str, "Act25SideData.AreaInfoData"]
    areaMissionData: dict[str, "Act25SideData.AreaMissionData"]
    battlePerformanceData: dict[str, "Act25SideData.BattlePerformanceData"]
    keyData: dict[str, "Act25SideData.KeyData"]
    fogUnlockData: dict[str, "Act25SideData.FogUnlockData"]
    farmList: list["Act25SideData.DailyFarmData"]

    class ConstData(BaseStruct):
        getDailyCount: int
        costName: str
        costDesc: str
        costLimit: int
        rewardLimit: int
        researchUnlockText: str
        harvestReward: ItemBundle
        costCount: int
        costCountLimit: int
        basicProgress: int
        harvestDesc: str

    class ZoneDescInfo(BaseStruct):
        zoneId: str
        unlockText: str
        displayStartTime: int

    class ArchiveItemData(BaseStruct):
        itemId: str
        itemType: "Act25SideData.Act25SideArchiveItemType"
        itemUnlockType: "Act25SideData.Act25SideArchiveItemUnlockType"
        itemUnlockParam: str | None
        unlockDesc: str | None
        iconId: str | None
        itemName: str

    class ArchiveMapInfoData(BaseStruct):
        objectId: str
        type_: "Act25SideData.Act25SideArchiveItemType" = field(name="type")
        numberId: str
        areaId: str
        sortId: int
        position: int
        hasDot: bool

    class AreaInfoData(BaseStruct):
        areaId: str
        sortId: int
        areaIcon: str
        areaName: str
        unlockText: str
        preposedStage: str
        areaInitialDesc: str
        areaEndingDesc: str
        areaEndingAud: str
        reward: ItemBundle
        finalId: str
        areaNewIcon: bool

    class AreaMissionData(BaseStruct):
        id_: str = field(name="id")
        areaId: str
        preposedMissionId: str | None
        sortId: int
        isZone: bool
        stageId: str
        costCount: int
        transform: int
        progress: int
        progressPicId: str
        template: str | None
        templateType: int
        desc: str
        param: list[str] | None
        rewards: list[ItemBundle]
        archiveItems: list[str]

    class BattlePerformanceData(BaseStruct):
        itemId: str
        sortId: int
        itemName: str
        itemIcon: str
        itemDesc: str
        itemTechType: "Act25SideData.Act25sideTechType"
        runeData: RuneTable.PackedRuneData

    class KeyData(BaseStruct):
        keyId: str
        keyName: str
        keyIcon: str
        toastText: str

    class FogUnlockData(BaseStruct):
        lockId: str
        lockedCollectionIconId: str
        unlockedCollectionIconId: str

    class DailyFarmData(BaseStruct):
        transform: int
        unitTime: int

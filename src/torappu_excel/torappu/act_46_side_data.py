from enum import StrEnum

from .item_bundle import ItemBundle
from ..common import BaseStruct


class Act46SideData(BaseStruct):
    zoneAdditionDataMap: dict[str, "Act46SideData.Act46SideZoneAdditionData"]
    monopolyStageDataMap: dict[str, "Act46SideData.Act46SideMonopolyStageData"]
    buffDataMap: dict[str, "Act46SideData.Act46SideMonopolyBuffData"]
    settleDialogDataMap: dict[str, dict[str, "list[Act46SideData.Act46SideSettleDialogData]"]]
    constData: "Act46SideData.Act46SideConstData"
    resourceItemDataMap: dict[str, "Act46SideData.Act46SideMonopolyResourceItemData"]

    class Act46SideSettleType(StrEnum):
        FAIL = "FAIL"
        GOOD = "GOOD"
        EXCELLENT = "EXCELLENT"

    class Act46SideZoneAdditionData(BaseStruct):
        zoneId: str
        unlockText: str

    class Act46SideMonopolyStageData(BaseStruct):
        stageId: str
        sortId: int
        startTs: int
        stageName: str
        stageDesc: str
        taskRequiredAmount: int
        rewardList: list[ItemBundle]
        buffIdList: list[str]
        bgSpriteId: str
        maxTurn: int
        nodeIconStyleIndexList: list[int]
        validResourceIdList: list[str]

    class Act46SideConstData(BaseStruct):
        trainingStageId: str
        excellentRate: list[int]
        entryRequirement: str
        businessUnlockText: str
        mapNodeStartIcon: str
        comboTaskProgressCount: int

    class Act46SideMonopolyBuffData(BaseStruct):
        buffId: str
        buffIconId: str
        buffName: str
        buffDesc: str

    class Act46SideSettleDialogData(BaseStruct):
        characterAvatarId: str
        dialogText: str

    class Act46SideMonopolyResourceItemData(BaseStruct):
        resourceId: str
        sortId: int

from .item_bundle import ItemBundle
from .item_type import ItemType
from ..common import BaseStruct


class ActVasebreakerData(BaseStruct):
    zoneAdditionDataMap: dict[str, "ActVasebreakerData.ActVasebreakerZoneAdditionData"]
    stageAdditionDataMap: dict[str, "ActVasebreakerData.ActVasebreakerStageAdditionData"]
    stageUnlockToastMap: dict[str, "ActVasebreakerData.ActVasebreakerStageUnlockToastData"]
    stageDropDataMap: dict[str, "ActVasebreakerData.ActVasebreakerStageDropData"]
    milestoneList: list["ActVasebreakerData.ActVasebreakerMilestoneItemData"]
    stickerList: list["ActVasebreakerData.ActVasebreakerStickerData"]
    constData: "ActVasebreakerData.ActVasebreakerConstData"

    class ActVasebreakerZoneAdditionData(BaseStruct):
        zoneId: str
        unlockText: str

    class ActVasebreakerStageAdditionData(BaseStruct):
        stageId: str
        firstCost: int
        formationMostNum: int
        formationLeastNum: int

    class ActVasebreakerStageUnlockToastData(BaseStruct):
        stageId: str
        unlockToast: str

    class ActVasebreakerStageDropData(BaseStruct):
        stageId: str
        itemType: ItemType
        itemId: str
        retryCount: int
        firstCount: int
        completeCount: int
        onceCompleteCount: int
        isDisplay: bool

    class ActVasebreakerMilestoneItemData(BaseStruct):
        milestoneId: str
        orderId: int
        tokenNum: int
        reward: ItemBundle
        availTime: int

    class ActVasebreakerStickerData(BaseStruct):
        stickerId: str
        stickerIcon: str
        template: str
        stickerName: str
        param: list[str]

    class ActVasebreakerConstData(BaseStruct):
        milestonePointId: str
        milestoneTrackId: str | None
        levelEntranceText: str
        rewardFurnitureId: str
        rewardFurnitureText: str
        rewardAvatarId: str
        rewardAvatarText: str

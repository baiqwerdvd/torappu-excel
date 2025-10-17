from .item_bundle import ItemBundle
from ..common import BaseStruct


class Act4D0Data(BaseStruct):
    mileStoneItemList: list["Act4D0Data.MileStoneItemInfo"]
    mileStoneStoryList: list["Act4D0Data.MileStoneStoryInfo"]
    storyInfoList: list["Act4D0Data.StoryInfo"]
    stageInfo: list["Act4D0Data.StageJumpInfo"]
    tokenItem: ItemBundle
    charStoneId: str
    apSupplyOutOfDateDict: dict[str, int]
    extraDropZones: list[str]

    class MileStoneItemInfo(BaseStruct):
        mileStoneId: str
        orderId: int
        tokenNum: int
        item: ItemBundle

    class MileStoneStoryInfo(BaseStruct):
        mileStoneId: str
        orderId: int
        tokenNum: int
        storyKey: str
        desc: str

    class StoryInfo(BaseStruct):
        storyKey: str
        storyId: str
        storySort: str
        storyName: str
        lockDesc: str
        storyDesc: str

    class StageJumpInfo(BaseStruct):
        stageKey: str
        zoneId: str
        stageId: str
        unlockDesc: str
        lockDesc: str

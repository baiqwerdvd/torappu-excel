from enum import StrEnum

from .item_type import ItemType
from ..common import BaseStruct


class ActivityCollectionData(BaseStruct):
    collections: list["ActivityCollectionData.CollectionInfo"]
    apSupplyOutOfDateDict: dict[str, int]
    consts: "ActivityCollectionData.Consts"

    class CollectionInfo(BaseStruct):
        id: int
        itemType: ItemType
        itemId: str
        itemCnt: int
        pointId: str
        pointCnt: int
        isBonus: bool
        pngName: str | None
        pngSort: int
        isShow: bool
        showInList: bool
        showIconBG: bool
        isBonusShow: bool

    class JumpType(StrEnum):
        NONE = "NONE"
        ROGUE = "ROGUE"
        CHAR_REPO = "CHAR_REPO"

    class Consts(BaseStruct):
        showJumpBtn: bool
        jumpBtnType: "ActivityCollectionData.JumpType"
        jumpBtnParam1: str | None
        jumpBtnParam2: str | None
        dailyTaskDisabled: bool
        dailyTaskStartTime: int
        isSimpleMode: bool

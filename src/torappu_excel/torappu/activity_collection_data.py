import enum

from .item_type import ItemType
from ..common import BaseStruct

from msgspec import field


class ActivityCollectionData(BaseStruct):
    collections: list["ActivityCollectionData.CollectionInfo"]
    apSupplyOutOfDateDict: dict[str, int]
    consts: "ActivityCollectionData.Consts"

    class CollectionInfo(BaseStruct):
        id_: int = field(name="id")
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

    class JumpType(enum.StrEnum):
        NONE = "NONE"
        ROGUE = "ROGUE"

    class Consts(BaseStruct):
        showJumpBtn: bool
        jumpBtnType: "ActivityCollectionData.JumpType"
        jumpBtnParam1: str | None
        jumpBtnParam2: str | None
        dailyTaskStartTime: int

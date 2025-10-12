from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .item_type import ItemType


class ActivityCollectionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    collections: list["ActivityCollectionData.CollectionInfo"]
    apSupplyOutOfDateDict: dict[str, int]
    consts: "ActivityCollectionData.Consts"

    class CollectionInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class Consts(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        showJumpBtn: bool
        jumpBtnType: "ActivityCollectionData.JumpType"
        jumpBtnParam1: str | None
        jumpBtnParam2: str | None
        dailyTaskDisabled: bool
        dailyTaskStartTime: int
        isSimpleMode: bool

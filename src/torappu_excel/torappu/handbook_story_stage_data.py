from .handbook_unlock_param import HandbookUnlockParam
from .item_bundle import ItemBundle
from ..common import BaseStruct

from msgspec import field


class HandbookStoryStageData(BaseStruct):
    charId: str
    code: str
    description: str
    levelId: str
    loadingPicId: str
    name: str
    rewardItem: list[ItemBundle]
    stageGetTime: int
    stageId: str
    unlockParam: list[HandbookUnlockParam]
    zoneId: str
    zoneNameForShow: str | None = field(default=None)
    stageNameForShow: str | None = field(default=None)
    picId: str | None = field(default=None)

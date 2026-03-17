from .item_bundle import ItemBundle
from .return_jump_type import ReturnJumpType
from ..common import BaseStruct


class ReturnMissionItemData(BaseStruct):
    missionId: str
    sortId: int
    uncompleteBgIcon: str
    completeBgIcon: str
    desc: str
    jumpType: ReturnJumpType
    jumpPlace: str | None
    rewardList: list[ItemBundle]

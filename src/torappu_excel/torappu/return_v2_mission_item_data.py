from .item_bundle import ItemBundle
from .return_v2_jump_type import ReturnV2JumpType
from ..common import BaseStruct


class ReturnV2MissionItemData(BaseStruct):
    missionId: str
    groupId: str
    sortId: int
    jumpType: ReturnV2JumpType
    jumpParam: str | None
    desc: str
    rewardList: list[ItemBundle]

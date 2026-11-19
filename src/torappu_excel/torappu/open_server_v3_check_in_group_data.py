from .item_bundle import ItemBundle
from .open_server_v3_check_in_item_data import OpenServerV3CheckInItemData
from ..common import BaseStruct


class OpenServerV3CheckInGroupData(BaseStruct):
    groupId: str
    specialRewardItem: ItemBundle
    specialRewardDay: int
    charImgId: str
    loginTitle: str
    loginDesc: str
    guidebookTrigger: str | None
    charList: list[str]
    checkInItemList: list[OpenServerV3CheckInItemData]

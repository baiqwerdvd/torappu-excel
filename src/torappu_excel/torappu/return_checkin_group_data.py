from .return_checkin_item_data import ReturnCheckinItemData
from ..common import BaseStruct


class ReturnCheckinGroupData(BaseStruct):
    groupId: str
    checkinItemList: list[ReturnCheckinItemData]

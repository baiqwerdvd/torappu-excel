from .open_server_v3_milestone_item_data import OpenServerV3MilestoneItemData
from ..common import BaseStruct


class OpenServerV3MilestoneGroupData(BaseStruct):
    groupId: str
    rewardImgId: str
    rewardItemId: str
    rewardPointId: str
    itemList: list[OpenServerV3MilestoneItemData]

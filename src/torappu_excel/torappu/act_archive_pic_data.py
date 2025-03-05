from .act_archive_pic_item_data import ActArchivePicItemData
from ..common import BaseStruct


class ActArchivePicData(BaseStruct):
    pics: dict[str, ActArchivePicItemData]

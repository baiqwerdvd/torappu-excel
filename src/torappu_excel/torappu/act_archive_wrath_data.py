from .act_archive_wrath_item_data import ActArchiveWrathItemData
from ..common import BaseStruct


class ActArchiveWrathData(BaseStruct):
    wraths: dict[str, ActArchiveWrathItemData]

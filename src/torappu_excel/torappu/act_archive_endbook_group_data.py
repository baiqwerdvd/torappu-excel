from .act_archive_endbook_item_data import ActArchiveEndbookItemData
from ..common import BaseStruct


class ActArchiveEndbookGroupData(BaseStruct):
    endId: str
    endingId: str
    sortId: int
    title: str
    cgId: str
    backBlurId: str
    cardId: str
    hasAvg: bool
    avgId: str
    clientEndbookItemDatas: list[ActArchiveEndbookItemData]

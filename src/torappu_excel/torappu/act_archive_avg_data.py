from .act_archive_avg_item_data import ActArchiveAvgItemData
from ..common import BaseStruct


class ActArchiveAvgData(BaseStruct):
    avgs: dict[str, ActArchiveAvgItemData]

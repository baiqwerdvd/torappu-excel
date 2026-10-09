from .act_archive_scrap_item_data import ActArchiveScrapItemData
from ..common import BaseStruct


class ActArchiveScrapData(BaseStruct):
    scraps: dict[str, ActArchiveScrapItemData]

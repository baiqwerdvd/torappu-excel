from .act_archive_fragment_item_data import ActArchiveFragmentItemData
from ..common import BaseStruct


class ActArchiveFragmentData(BaseStruct):
    fragment: dict[str, ActArchiveFragmentItemData]

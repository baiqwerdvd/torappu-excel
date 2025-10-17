from .act_archive_capsule_item_data import ActArchiveCapsuleItemData
from ..common import BaseStruct


class ActArchiveCapsuleData(BaseStruct):
    capsule: dict[str, ActArchiveCapsuleItemData]

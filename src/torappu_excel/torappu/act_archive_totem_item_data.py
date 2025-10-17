from .act_archive_totem_type import ActArchiveTotemType
from ..common import BaseStruct


class ActArchiveTotemItemData(BaseStruct):
    id: str
    type: ActArchiveTotemType
    enrollConditionId: str | None
    sortId: int

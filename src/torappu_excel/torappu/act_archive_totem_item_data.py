from .act_archive_totem_type import ActArchiveTotemType
from ..common import BaseStruct

from msgspec import field


class ActArchiveTotemItemData(BaseStruct):
    id_: str = field(name="id")
    type_: ActArchiveTotemType = field(name="type")
    enrollConditionId: str | None
    sortId: int

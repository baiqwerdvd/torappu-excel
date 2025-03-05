from ..common import BaseStruct

from msgspec import field


class ActArchiveChaosItemData(BaseStruct):
    id_: str = field(name="id")
    isHidden: bool
    enrollId: str | None
    sortId: int

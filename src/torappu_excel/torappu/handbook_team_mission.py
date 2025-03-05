from .item_bundle import ItemBundle
from ..common import BaseStruct

from msgspec import field


class HandbookTeamMission(BaseStruct):
    id_: str = field(name="id")
    sort: int
    powerId: str
    powerName: str
    item: ItemBundle
    favorPoint: int

from .item_bundle import ItemBundle
from ..common import BaseStruct


class HandbookTeamMission(BaseStruct):
    id: str
    sort: int
    powerId: str
    powerName: str
    item: ItemBundle
    favorPoint: int

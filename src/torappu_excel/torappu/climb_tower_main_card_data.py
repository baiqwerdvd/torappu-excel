from .climb_tower_card_type import ClimbTowerCardType
from .rune_table import RuneTable
from ..common import BaseStruct

from msgspec import field


class ClimbTowerMainCardData(BaseStruct):
    id_: str = field(name="id")
    type_: ClimbTowerCardType = field(name="type")
    linkedTowerId: str | None
    sortId: int
    name: str
    desc: str
    subCardIds: list[str]
    runeData: RuneTable.PackedRuneData | None
    trapIds: list[str]

from .climb_tower_card_type import ClimbTowerCardType
from .rune_table import RuneTable
from ..common import BaseStruct


class ClimbTowerMainCardData(BaseStruct):
    id: str
    type: ClimbTowerCardType
    linkedTowerId: str | None
    sortId: int
    name: str
    desc: str
    subCardIds: list[str]
    runeData: RuneTable.PackedRuneData | None
    trapIds: list[str]

from .rune_table import RuneTable
from ..common import BaseStruct


class ClimbTowerSubCardData(BaseStruct):
    id: str
    mainCardId: str
    sortId: int
    name: str
    desc: str
    runeData: RuneTable.PackedRuneData | None
    trapIds: list[str]

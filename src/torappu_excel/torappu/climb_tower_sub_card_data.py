from .rune_table import RuneTable
from ..common import BaseStruct

from msgspec import field


class ClimbTowerSubCardData(BaseStruct):
    id_: str = field(name="id")
    mainCardId: str
    sortId: int
    name: str
    desc: str
    runeData: RuneTable.PackedRuneData | None
    trapIds: list[str]

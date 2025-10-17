from .rune_table import RuneTable
from ..common import BaseStruct


class Act1VHalfIdleCharBuffInfo(BaseStruct):
    id: str
    level: int
    charCount: int
    desc: str
    runeData: "RuneTable.PackedRuneData"

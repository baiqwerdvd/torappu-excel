from .rune_table import RuneTable
from ..common import BaseStruct


class RecalRuneRuneData(BaseStruct):
    runeId: str
    score: int
    sortId: int
    essential: bool
    exclusiveGroupId: str | None
    runeIcon: str | None
    packedRune: "RuneTable.PackedRuneData"

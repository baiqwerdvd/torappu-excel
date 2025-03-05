from .rune_table import RuneTable
from ..common import BaseStruct


class ActVecBreakBattleBuffData(BaseStruct):
    buffId: str
    openTime: int
    name: str
    desc: str
    iconId: str
    runeData: "RuneTable.PackedRuneData"

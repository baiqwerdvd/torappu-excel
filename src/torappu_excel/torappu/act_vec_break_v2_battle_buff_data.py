from .rune_table import RuneTable
from ..common import BaseStruct


class ActVecBreakV2BattleBuffData(BaseStruct):
    buffId: str
    name: str
    desc: str
    iconId: str
    runeData: "RuneTable.PackedRuneData"

from .rune_table import RuneTable
from ..common import BaseStruct


class ActMultiV3SquadEffectData(BaseStruct):
    id: str
    iconId: str
    sortId: int
    name: str
    themeColor: str
    buffDesc: str
    debuffDesc: str
    token: "ActMultiV3SquadEffectData.Token"
    unlockKeyNum: int
    runeData: "RuneTable.PackedRuneData"

    class Token(BaseStruct):
        name: str
        desc: str
        iconId: str

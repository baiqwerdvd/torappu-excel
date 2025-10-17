from .roguelike_buff import RoguelikeBuff
from ..common import BaseStruct


class RoguelikeGameSquadBuffData(BaseStruct):
    id: str
    iconId: str
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    buffs: list[RoguelikeBuff]

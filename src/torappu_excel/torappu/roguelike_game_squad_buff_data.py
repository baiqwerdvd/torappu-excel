from .roguelike_buff import RoguelikeBuff
from ..common import BaseStruct

from msgspec import field


class RoguelikeGameSquadBuffData(BaseStruct):
    id_: str = field(name="id")
    iconId: str
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    buffs: list[RoguelikeBuff]

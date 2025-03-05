from .roguelike_buff import RoguelikeBuff
from ..common import BaseStruct

from msgspec import field


class RoguelikeGameRelicData(BaseStruct):
    id_: str = field(name="id")
    buffs: list[RoguelikeBuff]

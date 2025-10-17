from .roguelike_buff import RoguelikeBuff
from ..common import BaseStruct


class RoguelikeGameRelicData(BaseStruct):
    id: str
    buffs: list[RoguelikeBuff]

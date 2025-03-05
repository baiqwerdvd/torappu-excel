from .roguelike_game_variation_type import RoguelikeGameVariationType
from ..common import BaseStruct

from msgspec import field


class RoguelikeGameVariationData(BaseStruct):
    id_: str = field(name="id")
    type_: RoguelikeGameVariationType = field(name="type")
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    iconId: str | None
    sound: str | None

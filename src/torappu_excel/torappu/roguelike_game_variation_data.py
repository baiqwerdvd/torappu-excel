from .roguelike_game_variation_type import RoguelikeGameVariationType
from ..common import BaseStruct


class RoguelikeGameVariationData(BaseStruct):
    id: str
    type: RoguelikeGameVariationType
    outerName: str
    innerName: str
    functionDesc: str
    desc: str
    iconId: str | None
    sound: str | None

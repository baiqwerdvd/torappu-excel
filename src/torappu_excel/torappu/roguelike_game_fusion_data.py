from .roguelike_game_variation_type import RoguelikeGameVariationType
from ..common import BaseStruct


class RoguelikeGameFusionData(BaseStruct):
    id: str
    type: RoguelikeGameVariationType
    name: str
    functionDesc: str
    desc: str

from .roguelike_game_relic_check_param import RoguelikeGameRelicCheckParam
from .roguelike_game_relic_check_type import RoguelikeGameRelicCheckType
from ..common import BaseStruct


class RoguelikeGameRelicParamData(BaseStruct):
    id: str
    checkCharBoxTypes: list[RoguelikeGameRelicCheckType]
    checkCharBoxParams: list[RoguelikeGameRelicCheckParam]

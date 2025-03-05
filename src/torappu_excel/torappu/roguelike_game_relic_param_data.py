from .roguelike_game_relic_check_param import RoguelikeGameRelicCheckParam
from .roguelike_game_relic_check_type import RoguelikeGameRelicCheckType
from ..common import BaseStruct

from msgspec import field


class RoguelikeGameRelicParamData(BaseStruct):
    id_: str = field(name="id")
    checkCharBoxTypes: list[RoguelikeGameRelicCheckType]
    checkCharBoxParams: list[RoguelikeGameRelicCheckParam]

from .dice_result_class import DiceResultClass
from .dice_result_show_type import DiceResultShowType
from ..common import BaseStruct


class RoguelikeDiceRuleData(BaseStruct):
    dicePointMax: int
    diceResultClass: DiceResultClass
    diceGroupId: str
    diceEventId: str
    resultDesc: str
    showType: DiceResultShowType
    canReroll: bool
    diceEndingScene: str
    diceEndingDesc: str
    sound: str

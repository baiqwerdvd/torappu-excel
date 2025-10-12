from pydantic import BaseModel, ConfigDict

from .dice_result_class import DiceResultClass
from .dice_result_show_type import DiceResultShowType


class RoguelikeDiceRuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

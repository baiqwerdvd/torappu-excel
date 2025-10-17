from ..common import BaseStruct


class Act5FunChoiceRewardData(BaseStruct):
    choiceId: str
    name: str
    percentage: float | int
    isSpecialStyle: bool

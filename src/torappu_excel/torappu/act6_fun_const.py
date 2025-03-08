from ..common import BaseStruct


class Act6FunConst(BaseStruct):
    defaultStage: str | None
    achievementMaxNumber: int
    specialNumber: int
    characterTipToast: str | None
    functionToastList: list[str] | None

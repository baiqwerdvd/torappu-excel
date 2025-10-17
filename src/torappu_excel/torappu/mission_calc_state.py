from ..common import BaseStruct


class MissionCalcState(BaseStruct):
    target: int
    value: int
    compare: str | None = None

from ..common import BaseStruct


class PlayerBuildingMessageLeaveSP(BaseStruct):
    lastWeek: int
    lastWeekSum: int
    thisWeek: int
    thisWeekSum: int

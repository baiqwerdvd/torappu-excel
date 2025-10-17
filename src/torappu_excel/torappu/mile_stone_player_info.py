from ..common import BaseStruct


class MileStonePlayerInfo(BaseStruct):
    points: dict[str, int]
    got: dict[str, "MileStonePlayerInfo.MileStoneRewardTicketItem"]

    class MileStoneRewardTicketItem(BaseStruct):
        ts: int
        count: int

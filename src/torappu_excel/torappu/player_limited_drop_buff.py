from ..common import BaseStruct


class PlayerLimitedDropBuff(BaseStruct):
    dailyUsage: dict[str, "PlayerLimitedDropBuff.DailyUsage"]
    inventory: dict[str, "PlayerLimitedDropBuff.LimitedBuffGroup"]

    class DailyUsage(BaseStruct):
        times: int
        ts: int

    class LimitedBuffGroup(BaseStruct):
        ts: int
        count: int

from ..common import BaseStruct


class PlayerBuildingMeetingBuff(BaseStruct):
    speed: float
    weight: dict[str, float | int]
    flag: dict[str, float | int]
    apCost: "PlayerBuildingMeetingBuff.ApCost"
    notOwned: float | int
    owned: float | int

    class ApCost(BaseStruct):
        self: dict[str, int]

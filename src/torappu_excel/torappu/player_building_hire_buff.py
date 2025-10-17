from ..common import BaseStruct


class PlayerBuildingHireBuff(BaseStruct):
    speed: float
    point: dict[str, int]
    meeting: "PlayerBuildingHireBuff.Meeting"
    stack: "PlayerBuildingHireBuff.Stack"
    apCost: "PlayerBuildingHireBuff.ApCost"

    class ApCost(BaseStruct):
        self: dict[str, int]

    class Meeting(BaseStruct):
        speedUp: float | int

    class Stack(BaseStruct):
        char: list["PlayerBuildingHireBuff.Stack.Char"]
        clueWeight: dict[str, int]

        class Char(BaseStruct):
            refresh: int

from msgspec import field

from ..common import BaseStruct


class PlayerBuildingControlBuff(BaseStruct):
    global_: "PlayerBuildingControlBuff.Global" = field(name="global")
    manufacture: "PlayerBuildingControlBuff.Manufacture"
    trading: "PlayerBuildingControlBuff.Trading"
    meeting: "PlayerBuildingControlBuff.Meeting"
    apCost: dict[str, int]
    point: dict[str, int]
    hire: "PlayerBuildingControlBuff.Hire"
    power: "PlayerBuildingControlBuff.Power"
    dormitory: "PlayerBuildingControlBuff.Dormitory"
    training: "PlayerBuildingControlBuff.Training"

    class Global(BaseStruct):
        apCost: int
        roomCnt: dict[str, int]

    class Manufacture(BaseStruct):
        speed: float | int
        sSpeed: float | int
        roomSpeed: dict[str, float | int]
        apCost: int

    class Trading(Manufacture):
        charSpeed: dict[str, float | int]
        charLimit: dict[str, int]
        roomLimit: dict[str, int]

    class Meeting(BaseStruct):
        clue: float | int
        speedUp: float | int
        sSpeed: float | int
        weight: dict[str, float | int]
        apCost: int
        notOwned: float | int

    class Hire(BaseStruct):
        spUp: "PlayerBuildingControlBuff.Hire.SpUp"
        apCost: int
        up: int

        class SpUp(BaseStruct):
            base: float | int
            up: float | int

    class Power(BaseStruct):
        apCost: int

    class Dormitory(BaseStruct):
        recover: int
        tagRecover: dict[str, int]

    class Training(BaseStruct):
        speed: float

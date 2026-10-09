from .easing_type import EasingType
from .turning_mode import TurningMode
from ..common import BaseStruct


class ArkventMovePresetData(BaseStruct):
    presetId: str
    accelEasingType: EasingType
    accelDuration: float
    accPower: float
    decEasingType: EasingType
    decDuration: float
    decPower: float
    turningMode: TurningMode
    momentumTurnSpeed: float
    momentumTurnSpeedLow: float

from ..common import CustomIntEnum


class ArkventCameraBlendStyle(CustomIntEnum):
    Default = "Default", 0
    Cut = "Cut", 1
    EaseInOut = "EaseInOut", 2
    EaseIn = "EaseIn", 3
    EaseOut = "EaseOut", 4
    HardIn = "HardIn", 5
    HardOut = "HardOut", 6
    Linear = "Linear", 7

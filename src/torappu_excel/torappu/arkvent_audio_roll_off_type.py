from ..common import CustomIntEnum


class ArkventAudioRollOffType(CustomIntEnum):
    LINEAR = "LINEAR", 0
    LOGARITHMIC = "LOGARITHMIC", 1
    THIRD_PARTY = "THIRD_PARTY", 2

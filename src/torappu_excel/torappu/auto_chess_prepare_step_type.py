from enum import StrEnum


class AutoChessPrepareStepType(StrEnum):
    NONE = "NONE"
    INFO_CHECK = "INFO_CHECK"
    BAND_CHECK = "BAND_CHECK"
    CUSTOM_CHECK = "CUSTOM_CHECK"
    BATTLE_CHECK = "BATTLE_CHECK"

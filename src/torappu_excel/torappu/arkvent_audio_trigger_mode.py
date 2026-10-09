from ..common import CustomIntEnum


class ArkventAudioTriggerMode(CustomIntEnum):
    NONE = "NONE", 0
    ONE_SHOT = "ONE_SHOT", 1
    PERIODIC = "PERIODIC", 2
    EXIT = "EXIT", 3

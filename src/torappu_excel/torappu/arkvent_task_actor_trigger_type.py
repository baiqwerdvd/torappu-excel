from ..common import CustomIntEnum


class ArkventTaskActorTriggerType(CustomIntEnum):
    NONE = "NONE", 0
    AUTO = "AUTO", 1
    ENTER = "ENTER", 2
    INTERACT = "INTERACT", 3
    AUTO_ONCE = "AUTO_ONCE", 4

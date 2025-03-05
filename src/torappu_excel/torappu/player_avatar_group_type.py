from ..common import CustomIntEnum


class PlayerAvatarGroupType(CustomIntEnum):
    NONE = "NONE", 0
    ASSISTANT = "ASSISTANT", 1
    DEFAULT = "DEFAULT", 2
    SPECIAL = "SPECIAL", 3
    ACTIVITY = "ACTIVITY", 4
    DYNAMIC = "DYNAMIC", 5

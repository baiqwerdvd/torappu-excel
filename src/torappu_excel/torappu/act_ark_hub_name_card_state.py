from ..common import CustomIntEnum


class ActArkHubNameCardState(CustomIntEnum):
    NONE = "NONE", -1
    BATTLE = "BATTLE", 0
    CAPTURE = "CAPTURE", 1
    MATCH = "MATCH", 2
    PIXEL = "PIXEL", 3
    INTERACT = "INTERACT", 4

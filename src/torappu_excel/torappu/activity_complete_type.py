from enum import StrEnum


class ActivityCompleteType(StrEnum):
    SPECIAL = "SPECIAL"
    CAN_COMPLETE = "CAN_COMPLETE"
    CANNOT_COMPLETE = "CANNOT_COMPLETE"

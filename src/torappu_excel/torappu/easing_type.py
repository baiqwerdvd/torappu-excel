from ..common import CustomIntEnum


class EasingType(CustomIntEnum):
    INSTANT = "INSTANT", 0
    LINEAR = "LINEAR", 1
    EASE_IN = "EASE_IN", 2
    EASE_OUT = "EASE_OUT", 3
    EASE_IN_OUT = "EASE_IN_OUT", 4
    EXPONENTIAL = "EXPONENTIAL", 5

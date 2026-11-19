from ..common import CustomIntEnum


class MapLayerMask(CustomIntEnum):
    ALL = "ALL", 0
    LAYER_A = "LAYER_A", 2
    LAYER_B = "LAYER_B", 4
    LAYER_C = "LAYER_C", 8
    LAYER_D = "LAYER_D", 16
    NONE = "NONE", 255

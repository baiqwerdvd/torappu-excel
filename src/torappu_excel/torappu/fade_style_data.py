from ..common import BaseStruct


class FadeStyleData(BaseStruct):
    styleName: str
    fadeinTime: float
    fadeoutTime: float
    fadeinType: str
    fadeoutType: str

from ..common import BaseStruct


class PixelMapParamData(BaseStruct):
    width: int
    height: int
    initColor: str
    htmlColors: list[str]

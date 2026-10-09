from .pixel_map_const_data import PixelMapConstData
from .pixel_map_param_data import PixelMapParamData
from ..common import BaseStruct


class PixelMapData(BaseStruct):
    paramMap: dict[str, PixelMapParamData]
    constData: PixelMapConstData

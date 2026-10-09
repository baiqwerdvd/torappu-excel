from .arkvent_bark_pool_data import ArkventBarkPoolData
from ..common import BaseStruct


class ArkventBarkData(BaseStruct):
    barkAreaRadius: float
    showAreaRadius: float
    barkPoolData: dict[str, ArkventBarkPoolData]

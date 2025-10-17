from .act1_vhalf_idle_gacha_pool_type import Act1VHalfIdleGachaPoolType
from ..common import BaseStruct


class Act1VHalfIdleGachaPoolData(BaseStruct):
    poolId: str
    itemId: str
    poolType: Act1VHalfIdleGachaPoolType
    sortId: int
    name: str
    charData: list[str]
    consumeData: list["Act1VHalfIdleGachaPoolData.ConsumeData"]

    class ConsumeData(BaseStruct):
        gachaTimes: int
        consume: int

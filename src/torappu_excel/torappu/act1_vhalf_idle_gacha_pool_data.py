from pydantic import BaseModel, ConfigDict

from .act1_vhalf_idle_gacha_pool_type import Act1VHalfIdleGachaPoolType


class Act1VHalfIdleGachaPoolData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    poolId: str
    itemId: str
    poolType: Act1VHalfIdleGachaPoolType
    sortId: int
    name: str
    charData: list[str]
    consumeData: list["Act1VHalfIdleGachaPoolData.ConsumeData"]

    class ConsumeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        gachaTimes: int
        consume: int

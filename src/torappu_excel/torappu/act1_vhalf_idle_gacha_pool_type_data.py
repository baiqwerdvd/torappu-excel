from pydantic import BaseModel, ConfigDict

from .act1_vhalf_idle_gacha_pool_type import Act1VHalfIdleGachaPoolType


class Act1VHalfIdleGachaPoolTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    poolType: Act1VHalfIdleGachaPoolType
    typeName: str
    desc: str
    sortId: int

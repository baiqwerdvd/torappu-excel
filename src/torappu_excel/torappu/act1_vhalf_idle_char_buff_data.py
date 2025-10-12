from pydantic import BaseModel, ConfigDict

from .act1_vhalf_idle_char_buff_info import Act1VHalfIdleCharBuffInfo
from .profession_category import ProfessionCategory


class Act1VHalfIdleCharBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    prof: ProfessionCategory
    buffInfos: list[Act1VHalfIdleCharBuffInfo]

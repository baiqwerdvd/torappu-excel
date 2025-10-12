from pydantic import BaseModel, ConfigDict

from .medal_expire_type import MedalExpireType


class MedalExpireTime(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    start: int
    end: int
    type: MedalExpireType

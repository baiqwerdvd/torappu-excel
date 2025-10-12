from pydantic import BaseModel, ConfigDict

from .blackboard import Blackboard


class SandboxV2RacingItemInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    racerItemId: str
    name: str
    iconId: str
    blackboard: list[Blackboard]

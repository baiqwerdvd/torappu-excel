from pydantic import BaseModel, ConfigDict

from .blackboard import Blackboard


class RoguelikeBuff(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    key: str
    blackboard: list[Blackboard]

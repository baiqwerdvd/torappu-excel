from pydantic import BaseModel, ConfigDict


class RL02DevelopmentLine(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    fromNode: str
    toNode: str
    fromNodeP: int
    fromNodeR: int
    toNodeP: int
    toNodeR: int
    enrollId: str | None

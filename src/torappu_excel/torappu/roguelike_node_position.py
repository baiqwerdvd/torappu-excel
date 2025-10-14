from pydantic import BaseModel, ConfigDict


class RoguelikeNodePosition(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    x: int
    y: int

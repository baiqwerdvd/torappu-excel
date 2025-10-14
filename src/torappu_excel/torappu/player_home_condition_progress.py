from pydantic import BaseModel, ConfigDict


class PlayerHomeConditionProgress(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    v: int
    t: int

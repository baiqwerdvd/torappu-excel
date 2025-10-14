from pydantic import BaseModel, ConfigDict


class PlayerNodeRollInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    count: int
    cost: int

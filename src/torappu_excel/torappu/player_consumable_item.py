from pydantic import BaseModel, ConfigDict


class PlayerConsumableItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    ts: int
    count: int

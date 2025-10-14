from pydantic import BaseModel, ConfigDict


class PlayerBuildingCharBubble(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    add: int
    ts: int

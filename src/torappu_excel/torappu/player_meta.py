from pydantic import BaseModel, ConfigDict


class PlayerMeta(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    version: int
    ts: int

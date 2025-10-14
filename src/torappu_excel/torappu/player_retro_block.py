from pydantic import BaseModel, ConfigDict


class PlayerRetroBlock(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    locked: bool
    open: bool

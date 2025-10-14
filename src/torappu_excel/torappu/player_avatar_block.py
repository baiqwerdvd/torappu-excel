from pydantic import BaseModel, ConfigDict


class PlayerAvatarBlock(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    ts: int
    src: str

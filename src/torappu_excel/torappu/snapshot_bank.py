from pydantic import BaseModel, ConfigDict, Field


class SnapshotBank(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    name: str
    targetSnapshot: str
    hookSoundFxBank: str
    delay: float
    duration: float
    targetFxBank: str | None = Field(default=None)

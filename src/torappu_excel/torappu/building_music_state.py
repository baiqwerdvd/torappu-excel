from pydantic import BaseModel, ConfigDict


class BuildingMusicState(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    progress: list[int] | None
    unlock: bool

from pydantic import BaseModel, ConfigDict

from .building_music_state import BuildingMusicState


class BuildingMusic(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    inUse: bool
    selected: str
    state: dict[str, BuildingMusicState]

from pydantic import BaseModel, ConfigDict


class ActArchiveMusicItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    musicId: str
    musicSortId: int

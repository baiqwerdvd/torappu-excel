from pydantic import BaseModel, ConfigDict


class ActArchiveLandmarkItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    landmarkId: str
    landmarkSortId: int

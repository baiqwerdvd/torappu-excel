from pydantic import BaseModel, ConfigDict


class ActArchiveStoryItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    storyId: str
    storySortId: int

from pydantic import BaseModel, ConfigDict, Field


class ActArchiveTimelineItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    timelineId: str
    timelineSortId: int
    timelineTitle: str
    timelineDes: str
    picIdList: list[str] | None = Field(default=None)
    audioIdList: list[str] | None = Field(default=None)
    avgIdList: list[str] | None = Field(default=None)
    storyIdList: list[str] | None = Field(default=None)
    newsIdList: list[str] | None = Field(default=None)

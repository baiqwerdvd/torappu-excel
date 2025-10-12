from pydantic import BaseModel, ConfigDict, Field

from .handbook_avg_group_data import HandbookAvgGroupData
from .handbook_story_view_data import HandBookStoryViewData


class HandbookInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charID: str
    infoName: str
    storyTextAudio: list[HandBookStoryViewData]
    handbookAvgList: list[HandbookAvgGroupData]
    isLimited: bool | None = Field(default=None)

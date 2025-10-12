from pydantic import BaseModel, ConfigDict


class StorylineConstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    recommendHideGuideGroupId: str
    tutorialSelectStorylineId: str
    mainlineStorylineId: str

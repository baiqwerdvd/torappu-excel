from pydantic import BaseModel, ConfigDict


class StoryVariantData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    plotTaskId: str
    spStoryId: str
    storyId: str
    priority: int
    startTime: int
    endTime: int
    template: str
    param: list[str]

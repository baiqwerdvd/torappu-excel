from ..common import BaseStruct


class StoryVariantData(BaseStruct):
    plotTaskId: str
    spStoryId: str
    storyId: str
    priority: int
    startTime: int
    endTime: int
    template: str
    param: list[str]

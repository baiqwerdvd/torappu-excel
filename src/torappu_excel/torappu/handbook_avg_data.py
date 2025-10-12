from pydantic import BaseModel, ConfigDict


class HandbookAvgData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    storyId: str
    storySetId: str
    storySort: int
    storyCanShow: bool
    storyIntro: str
    storyInfo: str
    storyTxt: str

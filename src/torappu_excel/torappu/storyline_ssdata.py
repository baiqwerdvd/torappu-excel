from pydantic import BaseModel, ConfigDict


class StorylineSSData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    name: str
    desc: str
    backgroundId: str
    tags: list[str]
    reopenActivityId: str | None
    retroActivityId: str | None
    isRecommended: bool
    recommendHideStageId: str | None
    overrideStageList: list[str] | None

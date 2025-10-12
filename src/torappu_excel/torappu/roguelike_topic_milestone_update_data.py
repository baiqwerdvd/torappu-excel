from pydantic import BaseModel, ConfigDict


class RoguelikeTopicMilestoneUpdateData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    updateTime: int
    endTime: int
    maxBpLevel: int
    maxBpCount: int
    maxDisplayBpCount: int

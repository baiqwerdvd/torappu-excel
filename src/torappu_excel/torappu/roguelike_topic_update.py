from pydantic import BaseModel, ConfigDict


class RoguelikeTopicUpdate(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    updateId: str
    topicUpdateTime: int
    topicEndTime: int

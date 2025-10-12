from pydantic import BaseModel, ConfigDict


class RoguelikeTopicChallengeTask(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    taskId: str
    taskDes: str
    completionClass: str
    completionParams: list[str]

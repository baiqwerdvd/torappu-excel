from pydantic import BaseModel, ConfigDict


class RoguelikeCommonDevDifficultyNodePairInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    frontNodes: list[str]
    nextNode: str

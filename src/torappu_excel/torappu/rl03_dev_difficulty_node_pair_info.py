from pydantic import BaseModel, ConfigDict


class RL03DevDifficultyNodePairInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    frontNode: str
    nextNode: str

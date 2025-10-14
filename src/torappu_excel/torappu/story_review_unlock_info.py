from pydantic import BaseModel, ConfigDict


class StoryReviewUnlockInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    uts: int
    rc: int

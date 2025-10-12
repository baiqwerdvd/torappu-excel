from pydantic import BaseModel, ConfigDict


class ActArchiveChallengeBookItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    storyId: str
    sortId: int

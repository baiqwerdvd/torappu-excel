from pydantic import BaseModel, ConfigDict


class StorylineMainlineSplitData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    iconId: str
    subName: str

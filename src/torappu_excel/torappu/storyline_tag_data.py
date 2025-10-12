from pydantic import BaseModel, ConfigDict


class StorylineTagData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    tagId: str
    sortId: int
    tagDesc: str
    textColor: str
    bkgColor: str

from pydantic import BaseModel, ConfigDict


class Act42SideFileData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    contentId: str
    sortId: int

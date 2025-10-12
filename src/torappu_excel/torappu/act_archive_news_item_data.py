from pydantic import BaseModel, ConfigDict


class ActArchiveNewsItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    newsId: str
    newsSortId: int

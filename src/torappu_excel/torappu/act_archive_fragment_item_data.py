from pydantic import BaseModel, ConfigDict


class ActArchiveFragmentItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    fragmentId: str
    sortId: int
    enrollConditionId: str | None

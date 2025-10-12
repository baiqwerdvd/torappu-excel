from pydantic import BaseModel, ConfigDict


class ActArchiveCapsuleItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    capsuleId: str
    capsuleSortId: int
    englishName: str
    enrollId: str | None

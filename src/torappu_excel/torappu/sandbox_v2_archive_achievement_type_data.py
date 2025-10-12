from pydantic import BaseModel, ConfigDict


class SandboxV2ArchiveAchievementTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    achievementType: str
    name: str
    sortId: int

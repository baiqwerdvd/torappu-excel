from pydantic import BaseModel, ConfigDict


class SandboxV2ArchiveAchievementData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    achievementType: list[str]
    raritySortId: int
    sortId: int
    name: str
    desc: str

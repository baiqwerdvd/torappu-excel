from pydantic import BaseModel, ConfigDict


class RoguelikeDifficultyUpgradeRelicData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    relicId: str
    equivalentGrade: int

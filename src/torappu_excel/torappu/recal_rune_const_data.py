from pydantic import BaseModel, ConfigDict


class RecalRuneConstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageCountPerSeason: int
    juniorRewardMedalCount: int
    seniorRewardMedalCount: int
    unlockLevelIds: list[str]

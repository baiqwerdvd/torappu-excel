from pydantic import BaseModel, ConfigDict


class MissionDailyRewards(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    dailyPoint: int
    weeklyPoint: int
    rewards: dict[str, dict[str, int]]

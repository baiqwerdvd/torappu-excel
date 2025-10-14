from pydantic import BaseModel, ConfigDict


class PlayerMonthlySubPer(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    monthlySubscriptionEndTime: int
    monthlySubscriptionStartTime: int

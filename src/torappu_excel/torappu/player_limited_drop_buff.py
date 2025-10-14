from pydantic import BaseModel, ConfigDict


class PlayerLimitedDropBuff(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    dailyUsage: dict[str, "PlayerLimitedDropBuff.DailyUsage"]
    inventory: dict[str, "PlayerLimitedDropBuff.LimitedBuffGroup"]

    class DailyUsage(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        times: int
        ts: int

    class LimitedBuffGroup(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        ts: int
        count: int

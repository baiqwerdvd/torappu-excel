from pydantic import BaseModel, ConfigDict


class Act5FunSettleStreakData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    count: int
    desc: str

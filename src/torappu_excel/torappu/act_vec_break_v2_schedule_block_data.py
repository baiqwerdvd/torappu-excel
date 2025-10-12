from pydantic import BaseModel, ConfigDict


class ActVecBreakV2ScheduleBlockData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    startTs: int
    endTs: int

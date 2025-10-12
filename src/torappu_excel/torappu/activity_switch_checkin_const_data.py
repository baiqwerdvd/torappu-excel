from pydantic import BaseModel, ConfigDict


class ActivitySwitchCheckinConstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    activityTime: str
    activityRule: str

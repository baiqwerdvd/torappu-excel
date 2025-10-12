from pydantic import BaseModel, ConfigDict


class HomeMultiFormTimeRuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    startHour: int

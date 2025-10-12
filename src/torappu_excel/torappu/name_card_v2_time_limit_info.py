from pydantic import BaseModel, ConfigDict


class NameCardV2TimeLimitInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    availStartTime: int
    availEndTime: int

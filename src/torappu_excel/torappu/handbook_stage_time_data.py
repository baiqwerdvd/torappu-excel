from pydantic import BaseModel, ConfigDict


class HandbookStageTimeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    timestamp: int
    charSet: list[str]

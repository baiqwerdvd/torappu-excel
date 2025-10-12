from pydantic import BaseModel, ConfigDict


class StageValidInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    startTs: int
    endTs: int

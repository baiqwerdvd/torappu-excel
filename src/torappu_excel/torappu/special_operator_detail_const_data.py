from pydantic import BaseModel, ConfigDict


class SpecialOperatorDetailConstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nextRoundBuffToast: str

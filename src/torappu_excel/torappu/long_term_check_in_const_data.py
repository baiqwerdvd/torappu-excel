from pydantic import BaseModel, ConfigDict


class LongTermCheckInConstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    startTs: int
    detailTitle: str
    detailDesc: str

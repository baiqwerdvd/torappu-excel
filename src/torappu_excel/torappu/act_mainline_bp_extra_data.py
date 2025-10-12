from pydantic import BaseModel, ConfigDict


class ActMainlineBpExtraData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    periodDataList: list["ActMainlineBpExtraData.ActMainlineBpExtraPeriodData"]

    class ActMainlineBpExtraPeriodData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        periodId: str
        startTs: int
        endTs: int

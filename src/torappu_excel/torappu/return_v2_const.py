from pydantic import BaseModel, ConfigDict


class ReturnV2Const(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    startTime: int
    unlockLv: int
    unlockStage: str
    permMissionTime: int
    pointId: str
    returnPriceDesc: str
    dailySupplyDesc: str
    oldGPId: str

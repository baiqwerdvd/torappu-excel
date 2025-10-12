from pydantic import BaseModel, ConfigDict


class ActMultiV3SailBoatLevelPoolData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    startBlockPool: str
    midBlockPool: str
    endBlockPool: str

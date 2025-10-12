from pydantic import BaseModel, ConfigDict


class ClimbTowerRewardInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageSort: int
    lowerItemCount: int
    higherItemCount: int

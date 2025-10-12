from pydantic import BaseModel, ConfigDict


class ActVecBreakV2StageRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    completeRewardCnt: int
    normalRewardCnt: int
    limitReward: "ActVecBreakV2StageRewardData.LimitedRewardData | None"

    class LimitedRewardData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        startTs: int
        endTs: int
        rewardCnt: int

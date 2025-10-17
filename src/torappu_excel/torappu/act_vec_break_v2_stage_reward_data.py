from ..common import BaseStruct


class ActVecBreakV2StageRewardData(BaseStruct):
    stageId: str
    completeRewardCnt: int
    normalRewardCnt: int
    limitReward: "ActVecBreakV2StageRewardData.LimitedRewardData | None"

    class LimitedRewardData(BaseStruct):
        startTs: int
        endTs: int
        rewardCnt: int

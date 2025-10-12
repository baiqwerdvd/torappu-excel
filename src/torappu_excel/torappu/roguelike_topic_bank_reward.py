from pydantic import BaseModel, ConfigDict

from .roguelike_topic_bank_reward_type import RoguelikeTopicBankRewardType


class RoguelikeTopicBankReward(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rewardId: str
    unlockGoldCnt: int
    rewardType: RoguelikeTopicBankRewardType
    desc: str

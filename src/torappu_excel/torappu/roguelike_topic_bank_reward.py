from .roguelike_topic_bank_reward_type import RoguelikeTopicBankRewardType
from ..common import BaseStruct


class RoguelikeTopicBankReward(BaseStruct):
    rewardId: str
    unlockGoldCnt: int
    rewardType: RoguelikeTopicBankRewardType
    desc: str

from .rl01_ending_text import RL01EndingText
from .roguelike_topic_dev import RoguelikeTopicDev
from .roguelike_topic_dev_token import RoguelikeTopicDevToken
from ..common import BaseStruct


class RL01CustomizeData(BaseStruct):
    developments: dict[str, RoguelikeTopicDev]
    developmentTokens: dict[str, RoguelikeTopicDevToken]
    endingText: RL01EndingText

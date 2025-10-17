from .rl03_dev_difficulty_node_info import RL03DevDifficultyNodeInfo
from .rl03_dev_raw_text_buff_group import RL03DevRawTextBuffGroup
from .rl03_development import RL03Development
from .rl03_difficulty_ext import RL03DifficultyExt
from .rl03_ending_text import RL03EndingText
from .roguelike_topic_dev_token import RoguelikeTopicDevToken
from ..common import BaseStruct


class RL03CustomizeData(BaseStruct):
    developments: dict[str, RL03Development]
    developmentsTokens: dict[str, RoguelikeTopicDevToken]
    developmentRawTextGroup: list[RL03DevRawTextBuffGroup]
    developmentsDifficultyNodeInfos: dict[str, RL03DevDifficultyNodeInfo]
    endingText: RL03EndingText
    difficulties: list[RL03DifficultyExt]

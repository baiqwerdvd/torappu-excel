from .roguelike_common_dev_difficulty_node_info import RoguelikeCommonDevDifficultyNodeInfo
from .roguelike_common_dev_raw_text_buff_group import RoguelikeCommonDevRawTextBuffGroup
from .roguelike_common_development import RoguelikeCommonDevelopment
from .roguelike_topic_dev_token import RoguelikeTopicDevToken
from ..common import BaseStruct


class RoguelikeCommonDevelopmentData(BaseStruct):
    developments: dict[str, RoguelikeCommonDevelopment]
    developmentsTokens: dict[str, RoguelikeTopicDevToken]
    developmentRawTextGroup: list[RoguelikeCommonDevRawTextBuffGroup]
    developmentsDifficultyNodeInfos: dict[str, RoguelikeCommonDevDifficultyNodeInfo]

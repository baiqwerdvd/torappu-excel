from .roguelike_module import RoguelikeModule
from .roguelike_topic_basic_data import RoguelikeTopicBasicData
from .roguelike_topic_const import RoguelikeTopicConst
from .roguelike_topic_customize_data import RoguelikeTopicCustomizeData
from .roguelike_topic_detail import RoguelikeTopicDetail
from ..common import BaseStruct


class RoguelikeTopicTable(BaseStruct):
    topics: dict[str, RoguelikeTopicBasicData]
    constant: RoguelikeTopicConst
    details: dict[str, RoguelikeTopicDetail]
    modules: dict[str, RoguelikeModule]
    customizeData: RoguelikeTopicCustomizeData

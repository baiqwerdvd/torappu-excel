from .roguelike_topic_dev_token_display_form import RoguelikeTopicDevTokenDisplayForm
from ..common import BaseStruct


class RoguelikeTopicDisplayItem(BaseStruct):
    displayType: str
    displayNum: int
    displayForm: RoguelikeTopicDevTokenDisplayForm
    tokenDesc: str
    sortId: int

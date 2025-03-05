from .roguelike_topic_dev_token_display_form import RoguelikeTopicDevTokenDisplayForm
from ..common import BaseStruct


class RoguelikeTopicDevToken(BaseStruct):
    sortId: int
    displayForm: RoguelikeTopicDevTokenDisplayForm
    tokenDesc: str

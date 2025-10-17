from msgspec import field

from .roguelike_month_chat_trig_type import RoguelikeMonthChatTrigTypeStr
from ..common import BaseStruct


class RoguelikeTopicConfig(BaseStruct):
    webBusType: str
    monthChatTrigType: RoguelikeMonthChatTrigTypeStr
    loadRewardHpDecoPlugin: bool
    loadRewardExtraInfoPlugin: bool
    loadCharCardPlugin: bool | None = field(default=None)

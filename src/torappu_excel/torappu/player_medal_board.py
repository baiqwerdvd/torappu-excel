from .name_card_medal_type import NameCardMedalType
from ..common import BaseStruct


class PlayerMedalBoard(BaseStruct):
    type: NameCardMedalType
    custom: str | None
    template: str
    templateMedalList: list[str]

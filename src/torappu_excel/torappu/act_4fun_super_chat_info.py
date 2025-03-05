from .act4fun_super_chat_type import Act4funSuperChatType
from ..common import BaseStruct


class Act4funSuperChatInfo(BaseStruct):
    superChatId: str
    chatType: Act4funSuperChatType
    userName: str
    iconId: str
    valueEffectId: str
    performId: str
    superChatTxt: str

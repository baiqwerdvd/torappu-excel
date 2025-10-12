from pydantic import BaseModel, ConfigDict

from .act4fun_super_chat_type import Act4funSuperChatType


class Act4funSuperChatInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    superChatId: str
    chatType: Act4funSuperChatType
    userName: str
    iconId: str
    valueEffectId: str
    performId: str
    superChatTxt: str

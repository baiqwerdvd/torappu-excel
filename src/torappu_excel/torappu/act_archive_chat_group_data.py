from pydantic import BaseModel, ConfigDict, Field

from .act_archive_chat_item_data import ActArchiveChatItemData


class ActArchiveChatGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    sortId: int
    chatItemList: list[ActArchiveChatItemData]
    clientChatItemData: list[ActArchiveChatItemData] | None = Field(default=None)
    numChat: int | None = Field(default=None)

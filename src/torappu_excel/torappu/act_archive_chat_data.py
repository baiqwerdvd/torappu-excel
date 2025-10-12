from pydantic import BaseModel, ConfigDict

from .act_archive_chat_group_data import ActArchiveChatGroupData


class ActArchiveChatData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    chat: dict[str, ActArchiveChatGroupData]

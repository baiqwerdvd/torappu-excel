from pydantic import BaseModel, ConfigDict

from .name_card_medal_type import NameCardMedalType


class PlayerMedalBoard(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: NameCardMedalType
    custom: str | None
    template: str
    templateMedalList: list[str]

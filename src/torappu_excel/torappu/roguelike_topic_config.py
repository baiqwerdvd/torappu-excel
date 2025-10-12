from pydantic import BaseModel, ConfigDict, Field

from .roguelike_month_chat_trig_type import RoguelikeMonthChatTrigTypeStr


class RoguelikeTopicConfig(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    webBusType: str
    monthChatTrigType: RoguelikeMonthChatTrigTypeStr
    loadRewardHpDecoPlugin: bool
    loadRewardExtraInfoPlugin: bool
    loadCharCardPlugin: bool | None = Field(default=None)

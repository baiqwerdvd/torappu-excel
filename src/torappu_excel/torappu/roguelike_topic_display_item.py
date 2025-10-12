from pydantic import BaseModel, ConfigDict

from .roguelike_topic_dev_token_display_form import RoguelikeTopicDevTokenDisplayForm


class RoguelikeTopicDisplayItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    displayType: str
    displayNum: int
    displayForm: RoguelikeTopicDevTokenDisplayForm
    tokenDesc: str
    sortId: int

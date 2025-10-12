from pydantic import BaseModel, ConfigDict

from .roguelike_topic_dev_token_display_form import RoguelikeTopicDevTokenDisplayForm


class RoguelikeTopicDevToken(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    sortId: int
    displayForm: RoguelikeTopicDevTokenDisplayForm
    tokenDesc: str

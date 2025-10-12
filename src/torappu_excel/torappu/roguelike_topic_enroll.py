from pydantic import BaseModel, ConfigDict

from .roguelike_enroll_type import RoguelikeEnrollType


class RoguelikeTopicEnroll(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enrollId: str
    enrollTime: int
    enrollType: RoguelikeEnrollType
    enrollNoticeEndTime: int

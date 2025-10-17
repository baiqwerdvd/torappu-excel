from .roguelike_enroll_type import RoguelikeEnrollType
from ..common import BaseStruct


class RoguelikeTopicEnroll(BaseStruct):
    enrollId: str
    enrollTime: int
    enrollType: RoguelikeEnrollType
    enrollNoticeEndTime: int

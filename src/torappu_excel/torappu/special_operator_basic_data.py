from .special_operator_target_type import SpecialOperatorTargetType
from ..common import BaseStruct


class SpecialOperatorBasicData(BaseStruct):
    soCharId: str
    sortId: int
    targetType: SpecialOperatorTargetType
    targetId: str
    targetTopicName: str
    bgId: str
    bgEffectId: str
    charEffectId: str
    typeIconId: str

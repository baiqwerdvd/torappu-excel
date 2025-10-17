from .special_operator_target_type import SpecialOperatorTargetType
from ..common import BaseStruct


class SpecialOperatorModeData(BaseStruct):
    type: SpecialOperatorTargetType
    typeName: str

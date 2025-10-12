from pydantic import BaseModel, ConfigDict

from .special_operator_target_type import SpecialOperatorTargetType


class SpecialOperatorBasicData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    soCharId: str
    sortId: int
    targetType: SpecialOperatorTargetType
    targetId: str
    targetTopicName: str
    bgId: str
    bgEffectId: str
    charEffectId: str
    typeIconId: str

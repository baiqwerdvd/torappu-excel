from pydantic import BaseModel, ConfigDict

from .special_operator_target_type import SpecialOperatorTargetType


class SpecialOperatorModeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: SpecialOperatorTargetType
    typeName: str

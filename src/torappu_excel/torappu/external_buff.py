from pydantic import BaseModel, ConfigDict

from .attribute_modifier_data import AttributeModifierData


class ExternalBuff(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    attributes: AttributeModifierData

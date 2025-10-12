from pydantic import BaseModel, ConfigDict

from torappu_excel.common import CustomIntEnum

from .abnormal_combo import AbnormalCombo
from .abnormal_flag import AbnormalFlag
from .attribute_type import AttributeType


class AttributeModifierData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    abnormalFlags: list[AbnormalFlag] | None
    abnormalImmunes: list[AbnormalFlag] | None
    abnormalAntis: list[AbnormalFlag] | None
    abnormalCombos: list[AbnormalCombo] | None
    abnormalComboImmunes: list[AbnormalCombo] | None
    attributeModifiers: list["AttributeModifierData.AttributeModifier"]

    class AttributeModifier(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        class FormulaItemType(CustomIntEnum):
            ADDITION = "ADDITION", 0
            MULTIPLIER = "MULTIPLIER", 1
            FINAL_ADDITION = "FINAL_ADDITION", 2
            FINAL_SCALER = "FINAL_SCALER", 3

        attributeType: AttributeType
        formulaItem: "AttributeModifierData.AttributeModifier.FormulaItemType"
        value: float
        loadFromBlackboard: bool
        fetchBaseValueFromSourceEntity: bool

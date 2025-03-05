from .abnormal_combo import AbnormalCombo
from .abnormal_flag import AbnormalFlag
from .attribute_type import AttributeType
from ..common import BaseStruct, CustomIntEnum


class AttributeModifierData(BaseStruct):
    abnormalFlags: list[AbnormalFlag] | None
    abnormalImmunes: list[AbnormalFlag] | None
    abnormalAntis: list[AbnormalFlag] | None
    abnormalCombos: list[AbnormalCombo] | None
    abnormalComboImmunes: list[AbnormalCombo] | None
    attributeModifiers: list["AttributeModifierData.AttributeModifier"]

    class AttributeModifier(BaseStruct):
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

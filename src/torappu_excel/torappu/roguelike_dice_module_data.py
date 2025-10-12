from pydantic import BaseModel, ConfigDict

from .roguelike_dice_data import RoguelikeDiceData
from .roguelike_dice_predefine_data import RoguelikeDicePredefineData
from .roguelike_dice_rule_data import RoguelikeDiceRuleData
from .roguelike_dice_rule_group_data import RoguelikeDiceRuleGroupData


class RoguelikeDiceModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    dice: dict[str, RoguelikeDiceData]
    diceEvents: dict[str, RoguelikeDiceRuleData]
    diceChoices: dict[str, str]
    diceRuleGroups: dict[str, RoguelikeDiceRuleGroupData]
    dicePredefines: list[RoguelikeDicePredefineData]

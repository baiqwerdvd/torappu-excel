from .roguelike_dice_data import RoguelikeDiceData
from .roguelike_dice_predefine_data import RoguelikeDicePredefineData
from .roguelike_dice_rule_data import RoguelikeDiceRuleData
from .roguelike_dice_rule_group_data import RoguelikeDiceRuleGroupData
from ..common import BaseStruct


class RoguelikeDiceModuleData(BaseStruct):
    dice: dict[str, RoguelikeDiceData]
    diceEvents: dict[str, RoguelikeDiceRuleData]
    diceChoices: dict[str, str]
    diceRuleGroups: dict[str, RoguelikeDiceRuleGroupData]
    dicePredefines: list[RoguelikeDicePredefineData]

from .roguelike_chaos_module_data import RoguelikeChaosModuleData
from .roguelike_dice_module_data import RoguelikeDiceModuleData
from .roguelike_disaster_module_data import RoguelikeDisasterModuleData
from .roguelike_fragment_module_data import RoguelikeFragmentModuleData
from .roguelike_module_type import RoguelikeModuleType
from .roguelike_node_upgrade_module_data import RoguelikeNodeUpgradeModuleData
from .roguelike_san_check_module_data import RoguelikeSanCheckModuleData
from .roguelike_totem_buff_module_data import RoguelikeTotemBuffModuleData
from .roguelike_vision_module_data import RoguelikeVisionModuleData
from ..common import BaseStruct

from msgspec import field


class RoguelikeModule(BaseStruct):
    moduleTypes: list[RoguelikeModuleType]
    sanCheck: RoguelikeSanCheckModuleData | None
    dice: RoguelikeDiceModuleData | None
    chaos: RoguelikeChaosModuleData | None
    totemBuff: RoguelikeTotemBuffModuleData | None
    vision: RoguelikeVisionModuleData | None
    fragment: RoguelikeFragmentModuleData | None = field(default=None)
    disaster: RoguelikeDisasterModuleData | None = field(default=None)
    nodeUpgrade: RoguelikeNodeUpgradeModuleData | None = field(default=None)

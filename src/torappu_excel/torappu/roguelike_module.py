from msgspec import field

from .roguelike_candle_module_data import RoguelikeCandleModuleData
from .roguelike_chaos_module_data import RoguelikeChaosModuleData
from .roguelike_copper_module_data import RoguelikeCopperModuleData
from .roguelike_dice_module_data import RoguelikeDiceModuleData
from .roguelike_disaster_module_data import RoguelikeDisasterModuleData
from .roguelike_fragment_module_data import RoguelikeFragmentModuleData
from .roguelike_module_type import RoguelikeModuleType
from .roguelike_node_upgrade_module_data import RoguelikeNodeUpgradeModuleData
from .roguelike_san_check_module_data import RoguelikeSanCheckModuleData
from .roguelike_sky_module_data import RoguelikeSkyModuleData
from .roguelike_totem_buff_module_data import RoguelikeTotemBuffModuleData
from .roguelike_vision_module_data import RoguelikeVisionModuleData
from .roguelike_wrath_module_data import RoguelikeWrathModuleData
from ..common import BaseStruct


class RoguelikeModule(BaseStruct):
    moduleTypes: list[RoguelikeModuleType]
    sanCheck: RoguelikeSanCheckModuleData | None
    dice: RoguelikeDiceModuleData | None
    chaos: RoguelikeChaosModuleData | None
    totemBuff: RoguelikeTotemBuffModuleData | None
    vision: RoguelikeVisionModuleData | None
    copper: RoguelikeCopperModuleData | None
    wrath: RoguelikeWrathModuleData | None
    candle: RoguelikeCandleModuleData | None
    sky: RoguelikeSkyModuleData | None
    fragment: RoguelikeFragmentModuleData | None = field(default=None)
    disaster: RoguelikeDisasterModuleData | None = field(default=None)
    nodeUpgrade: RoguelikeNodeUpgradeModuleData | None = field(default=None)

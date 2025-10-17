from .roguelike_totem_buff_data import RoguelikeTotemBuffData
from .roguelike_totem_module_consts import RoguelikeTotemModuleConsts
from .roguelike_totem_sub_buff_data import RoguelikeTotemSubBuffData
from ..common import BaseStruct


class RoguelikeTotemBuffModuleData(BaseStruct):
    totemBuffDatas: dict[str, RoguelikeTotemBuffData]
    subBuffs: dict[str, RoguelikeTotemSubBuffData]
    moduleConsts: RoguelikeTotemModuleConsts

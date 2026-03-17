from .roguelike_copper_data import RoguelikeCopperData
from .roguelike_copper_divine_data import RoguelikeCopperDivineData
from .roguelike_copper_gild_type_data import RoguelikeCopperGildTypeData
from .roguelike_copper_module_consts import RoguelikeCopperModuleConsts
from ..common import BaseStruct


class RoguelikeCopperModuleData(BaseStruct):
    copperData: dict[str, RoguelikeCopperData]
    copperDivineData: dict[str, RoguelikeCopperDivineData]
    copperGildTypeData: dict[str, RoguelikeCopperGildTypeData]
    changeCopperMap: dict[str, str]
    moduleConsts: RoguelikeCopperModuleConsts

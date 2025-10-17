from .roguelike_wrath_data import RoguelikeWrathData
from .roguelike_wrath_module_consts import RoguelikeWrathModuleConsts
from ..common import BaseStruct


class RoguelikeWrathModuleData(BaseStruct):
    wrathData: dict[str, RoguelikeWrathData]
    moduleConsts: RoguelikeWrathModuleConsts

from .name_card_v2_consts import NameCardV2Consts
from .name_card_v2_module_data import NameCardV2ModuleData
from .name_card_v2_removable_module_data import NameCardV2RemovableModuleData
from .name_card_v2_skin_data import NameCardV2SkinData
from ..common import BaseStruct


class NameCardV2Data(BaseStruct):
    fixedModuleData: dict[str, NameCardV2ModuleData]
    removableModuleData: dict[str, NameCardV2RemovableModuleData]
    skinData: dict[str, NameCardV2SkinData]
    consts: NameCardV2Consts

from .name_card_v2_module_sub_type import NameCardV2ModuleSubType
from .name_card_v2_module_type import NameCardV2ModuleType
from ..common import BaseStruct


class NameCardV2RemovableModuleData(BaseStruct):
    id: str
    type: NameCardV2ModuleType
    sortId: int
    subType: NameCardV2ModuleSubType
    name: str

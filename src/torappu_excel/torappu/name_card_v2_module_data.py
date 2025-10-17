from .name_card_v2_module_type import NameCardV2ModuleType
from ..common import BaseStruct


class NameCardV2ModuleData(BaseStruct):
    id: str
    type: NameCardV2ModuleType

from .name_card_v2_module_type import NameCardV2ModuleType
from ..common import BaseStruct

from msgspec import field


class NameCardV2ModuleData(BaseStruct):
    id_: str = field(name="id")
    type_: NameCardV2ModuleType = field(name="type")

from .act_ark_hub_module_type import ActArkHubModuleType
from .arkdex_module_data import ArkdexModuleData
from .arkpixel_module_data import ArkpixelModuleData
from ..common import BaseStruct


class ActArkHubModuleData(BaseStruct):
    arkdexModule: ArkdexModuleData
    arkpixelModule: ArkpixelModuleData
    moduleTypes: list[ActArkHubModuleType]

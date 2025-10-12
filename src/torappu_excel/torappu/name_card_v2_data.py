from pydantic import BaseModel, ConfigDict

from .name_card_v2_consts import NameCardV2Consts
from .name_card_v2_module_data import NameCardV2ModuleData
from .name_card_v2_removable_module_data import NameCardV2RemovableModuleData
from .name_card_v2_skin_data import NameCardV2SkinData


class NameCardV2Data(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    fixedModuleData: dict[str, NameCardV2ModuleData]
    removableModuleData: dict[str, NameCardV2RemovableModuleData]
    skinData: dict[str, NameCardV2SkinData]
    consts: NameCardV2Consts

from pydantic import BaseModel, ConfigDict

from .name_card_v2_module_sub_type import NameCardV2ModuleSubType
from .name_card_v2_module_type import NameCardV2ModuleType


class NameCardV2RemovableModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: NameCardV2ModuleType
    sortId: int
    subType: NameCardV2ModuleSubType
    name: str

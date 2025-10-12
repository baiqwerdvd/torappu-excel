from pydantic import BaseModel, ConfigDict

from .name_card_v2_module_type import NameCardV2ModuleType


class NameCardV2ModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: NameCardV2ModuleType

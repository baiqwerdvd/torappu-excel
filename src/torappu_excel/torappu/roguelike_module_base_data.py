from pydantic import BaseModel, ConfigDict

from .roguelike_module_type import RoguelikeModuleType


class RoguelikeModuleBaseData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    moduleType: RoguelikeModuleType

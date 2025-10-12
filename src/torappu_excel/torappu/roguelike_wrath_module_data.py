from pydantic import BaseModel, ConfigDict

from .roguelike_wrath_data import RoguelikeWrathData
from .roguelike_wrath_module_consts import RoguelikeWrathModuleConsts


class RoguelikeWrathModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    wrathData: dict[str, RoguelikeWrathData]
    moduleConsts: RoguelikeWrathModuleConsts

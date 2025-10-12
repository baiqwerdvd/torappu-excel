from pydantic import BaseModel, ConfigDict

from .roguelike_copper_data import RoguelikeCopperData
from .roguelike_copper_divine_data import RoguelikeCopperDivineData
from .roguelike_copper_module_consts import RoguelikeCopperModuleConsts


class RoguelikeCopperModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    copperData: dict[str, RoguelikeCopperData]
    copperDivineData: dict[str, RoguelikeCopperDivineData]
    changeCopperMap: dict[str, str]
    moduleConsts: RoguelikeCopperModuleConsts

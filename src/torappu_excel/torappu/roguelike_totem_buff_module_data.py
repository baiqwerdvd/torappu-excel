from pydantic import BaseModel, ConfigDict

from .roguelike_totem_buff_data import RoguelikeTotemBuffData
from .roguelike_totem_module_consts import RoguelikeTotemModuleConsts
from .roguelike_totem_sub_buff_data import RoguelikeTotemSubBuffData


class RoguelikeTotemBuffModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    totemBuffDatas: dict[str, RoguelikeTotemBuffData]
    subBuffs: dict[str, RoguelikeTotemSubBuffData]
    moduleConsts: RoguelikeTotemModuleConsts

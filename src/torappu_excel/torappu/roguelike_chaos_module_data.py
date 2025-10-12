from pydantic import BaseModel, ConfigDict

from .roguelike_chaos_data import RoguelikeChaosData
from .roguelike_chaos_module_consts import RoguelikeChaosModuleConsts
from .roguelike_chaos_predefine_level_info import RoguelikeChaosPredefineLevelInfo
from .roguelike_chaos_range_data import RoguelikeChaosRangeData


class RoguelikeChaosModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    chaosDatas: dict[str, RoguelikeChaosData]
    chaosRanges: list[RoguelikeChaosRangeData]
    levelInfoDict: dict[str, dict[str, RoguelikeChaosPredefineLevelInfo]]
    moduleConsts: RoguelikeChaosModuleConsts

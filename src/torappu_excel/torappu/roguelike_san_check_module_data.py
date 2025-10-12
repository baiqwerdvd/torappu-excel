from pydantic import BaseModel, ConfigDict

from .roguelike_san_check_consts import RoguelikeSanCheckConsts
from .roguelike_san_range_data import RoguelikeSanRangeData


class RoguelikeSanCheckModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    sanRanges: list[RoguelikeSanRangeData]
    moduleConsts: RoguelikeSanCheckConsts

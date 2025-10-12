from pydantic import BaseModel, ConfigDict

from .tip_data import TipData
from .world_view_tip import WorldViewTip


class TipTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    tips: list[TipData]
    worldViewTips: list[WorldViewTip]

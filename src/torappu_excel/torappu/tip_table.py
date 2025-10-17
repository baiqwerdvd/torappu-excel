from .tip_data import TipData
from .world_view_tip import WorldViewTip
from ..common import BaseStruct


class TipTable(BaseStruct):
    tips: list[TipData]
    worldViewTips: list[WorldViewTip]

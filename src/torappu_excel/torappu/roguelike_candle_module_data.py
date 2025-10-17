from .roguelike_candle_module_consts import RoguelikeCandleModuleConsts
from ..common import BaseStruct


class RoguelikeCandleModuleData(BaseStruct):
    candleTicketIdList: list[str]
    moduleConsts: RoguelikeCandleModuleConsts
    candleBattleStageIdList: list[str]

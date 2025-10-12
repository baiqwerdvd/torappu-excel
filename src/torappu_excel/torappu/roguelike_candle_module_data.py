from pydantic import BaseModel, ConfigDict

from .roguelike_candle_module_consts import RoguelikeCandleModuleConsts


class RoguelikeCandleModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    candleTicketIdList: list[str]
    moduleConsts: RoguelikeCandleModuleConsts
    candleBattleStageIdList: list[str]

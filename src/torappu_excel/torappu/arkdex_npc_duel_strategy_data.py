from .ark_dex_npc_card_strategy import ArkDexNpcCardStrategy
from .ark_dex_npc_tile_strategy import ArkDexNpcTileStrategy
from .arkdex_npc_duel_creature_data import ArkdexNpcDuelCreatureData
from ..common import BaseStruct


class ArkdexNpcDuelStrategyData(BaseStruct):
    strategyGroupId: str
    strategyId: str
    tileStrategy: ArkDexNpcTileStrategy
    cardStrategy: ArkDexNpcCardStrategy
    creatureData: list[ArkdexNpcDuelCreatureData]
    weight: int

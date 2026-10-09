from .arkdex_advantage_type_data import ArkdexAdvantageTypeData
from .arkdex_capture_area_data import ArkdexCaptureAreaData
from .arkdex_const_data import ArkdexConstData
from .arkdex_creature_data import ArkdexCreatureData
from .arkdex_item_effect_data import ArkdexItemEffectData
from .arkdex_mode_data import ArkdexModeData
from .arkdex_npc_battle_param_data import ArkdexNpcBattleParamData
from .arkdex_npc_duel_strategy_data import ArkdexNpcDuelStrategyData
from .arkdex_npc_info_data import ArkdexNpcInfoData
from .arkdex_npc_pixel_data import ArkdexNpcPixelData
from .arkdex_trait_data import ArkdexTraitData
from ..common import BaseStruct


class ArkdexModuleData(BaseStruct):
    modeData: dict[str, ArkdexModeData]
    creatureData: dict[str, ArkdexCreatureData]
    advantageTypeData: dict[str, ArkdexAdvantageTypeData]
    advantageCounterMap: dict[str, list[str]]
    npcInfoData: dict[str, ArkdexNpcInfoData]
    npcDuelStrategyData: dict[str, dict[str, ArkdexNpcDuelStrategyData]]
    itemEffectData: dict[str, ArkdexItemEffectData]
    traitData: dict[str, ArkdexTraitData]
    sceneTypeMap: dict[str, str]
    npcBattleParamData: dict[str, ArkdexNpcBattleParamData]
    npcPixelData: dict[str, ArkdexNpcPixelData]
    captureAreaData: dict[str, ArkdexCaptureAreaData]
    dexConstData: ArkdexConstData

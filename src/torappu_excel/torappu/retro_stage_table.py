from msgspec import field

from .activity_custom_data import ActivityCustomData
from .retro_act_data import RetroActData
from .retro_stage_override_info import RetroStageOverrideInfo
from .retro_trail_data import RetroTrailData
from .retro_trail_rule_data import RetroTrailRuleData
from .stage_data import StageData
from .stage_valid_info import StageValidInfo
from ..common import BaseStruct


class RetroStageTable(BaseStruct):
    zoneToRetro: dict[str, str]
    stageValidInfo: dict[str, StageValidInfo]
    retroActList: dict[str, RetroActData]
    retroTrailList: dict[str, RetroTrailData]
    stageList: dict[str, StageData]
    ruleData: RetroTrailRuleData
    customData: ActivityCustomData
    initRetroCoin: int
    retroCoinPerWeek: int
    retroCoinMaxOfLevels: dict[str, int]
    retroDetail: str
    retroPreShowTime: int
    retroUnlockCost: int
    stages: dict[str, RetroStageOverrideInfo] | None = field(default=None)
    retroCoinMax: int | None = field(default=None)

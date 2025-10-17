from msgspec import field

from .ap_protect_zone_info import ApProtectZoneInfo
from .conditional_drop_info import ConditionalDropInfo
from .map_theme_data import MapThemeData
from .override_drop_info import OverrideDropInfo
from .override_unlock_info import OverrideUnlockInfo
from .record_reward_server_data import RecordRewardServerData
from .rune_stage_group_data import RuneStageGroupData
from .six_star_linked_stage_compatible_info import SixStarLinkedStageCompatibleInfo
from .six_star_milestone_group_data import SixStarMilestoneGroupData
from .six_star_rune_data import SixStarRuneData
from .special_battle_finish_stage_data import SpecialBattleFinishStageData
from .stage_data import StageData
from .stage_diff_group import StageDiffGroup
from .stage_diff_group_table import StageDiffGroupTable
from .stage_fog_info import StageFogInfo
from .stage_start_cond import StageStartCond
from .stage_valid_info import StageValidInfo
from .story_stage_show_group import StoryStageShowGroup
from .storyline_const_data import StorylineConstData
from .storyline_data import StorylineData
from .storyline_story_set_data import StorylineStorySetData
from .storyline_tag_data import StorylineTagData
from .tile_append_info import TileAppendInfo
from .timely_drop_info import TimelyDropInfo
from .timely_drop_time_info import TimelyDropTimeInfo
from .weekly_force_open_table import WeeklyForceOpenTable
from ..common import BaseStruct


class StageTable(BaseStruct):
    stages: dict[str, StageData]
    runeStageGroups: dict[str, RuneStageGroupData]
    mapThemes: dict[str, MapThemeData]
    tileInfo: dict[str, TileAppendInfo]
    forceOpenTable: dict[str, WeeklyForceOpenTable]
    timelyStageDropInfo: dict[str, TimelyDropTimeInfo]
    overrideDropInfo: dict[str, OverrideDropInfo]
    timelyTable: dict[str, TimelyDropInfo]
    stageValidInfo: dict[str, StageValidInfo]
    stageFogInfo: dict[str, StageFogInfo]
    stageStartConds: dict[str, StageStartCond]
    diffGroupTable: dict[str, StageDiffGroupTable]
    storyStageShowGroup: dict[str, dict[StageDiffGroup, StoryStageShowGroup]]
    specialBattleFinishStageData: dict[str, SpecialBattleFinishStageData]
    recordRewardData: dict[str, RecordRewardServerData] | None
    apProtectZoneInfo: dict[str, ApProtectZoneInfo]
    actCustomStageDatas: dict[str, dict[str, str]]
    spNormalStageIdFor4StarList: list[str]
    antiSpoilerDict: dict[str, list[str]]
    storylines: dict[str, StorylineData]
    storylineStorySets: dict[str, StorylineStorySetData]
    storylineTags: dict[str, StorylineTagData]
    storylineConst: StorylineConstData
    sixStarRuneData: dict[str, SixStarRuneData]
    sixStarMilestoneInfo: dict[str, SixStarMilestoneGroupData]
    sixStarCompatibleInfo: dict[str, SixStarLinkedStageCompatibleInfo]
    conditionalDropInfo: dict[str, ConditionalDropInfo]
    overrideUnlockInfo: dict[str, OverrideUnlockInfo] = field(default_factory=dict)

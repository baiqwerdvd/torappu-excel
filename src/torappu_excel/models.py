from .common import BaseStruct
from .torappu.activity_table import ActivityTable as ActivityTable_
from .torappu.audio_data import AudioData as AudioData
from .torappu.battle_equip_pack import BattleEquipPack
from .torappu.building_data import BuildingData as BuildingData
from .torappu.campaign_table import CampaignTable as CampaignTable_
from .torappu.chapter_data import ChapterData
from .torappu.char_meta_table import CharMetaTable as CharMetaTable_
from .torappu.char_patch_table import CharPatchData
from .torappu.character_data import CharacterData, MasterDataBundle, TokenCharacterData
from .torappu.charm_data import CharmData
from .torappu.charword_table import CharwordTable as CharwordTable_
from .torappu.checkin_table import CheckinTable as CheckinTable_
from .torappu.climb_tower_table import ClimbTowerTable as ClimbTowerTable_
from .torappu.crisis_table import CrisisTable as CrisisTable_
from .torappu.crisis_v2_shared_data import CrisisV2SharedData
from .torappu.display_meta_data import DisplayMetaData
from .torappu.enemy_handbook_data_group import EnemyHandBookDataGroup
from .torappu.favor_table import FavorTable as FavorTable_
from .torappu.gacha_data import GachaData
from .torappu.game_data_consts import GameDataConsts
from .torappu.handbook_info_table import HandbookInfoTable as HandbookInfoTable_
from .torappu.handbook_table import HandbookTable as HandbookTable_
from .torappu.handbook_team_data import HandbookTeamData
from .torappu.medal_data import MedalData
from .torappu.meeting_clue_data import MeetingClueData as MeetingClueData
from .torappu.mission_table import MissionTable as MissionTable_
from .torappu.open_server_schedule import OpenServerSchedule
from .torappu.player_avatar_data import PlayerAvatarData
from .torappu.range_data import RangeData
from .torappu.replicate_table import ReplicateTable as ReplicateTable_
from .torappu.retro_stage_table import RetroStageTable
from .torappu.roguelike_table import RoguelikeTable as RoguelikeTable_
from .torappu.roguelike_topic_table import RoguelikeTopicTable as RoguelikeTopicTable_
from .torappu.rune_table import RuneTable
from .torappu.sandbox_perm_table import SandboxPermTable as SandboxPermTable_
from .torappu.sandbox_table import SandboxTable as SandboxTable_
from .torappu.server_item_table import ServerItemTable
from .torappu.shop_client_data import ShopClientData
from .torappu.skill_data_bundle import SkillDataBundle
from .torappu.skin_table import SkinTable as SkinTable_
from .torappu.special_operator_table import SpecialOperatorTable as SpecialOperatorTable_
from .torappu.stage_table import StageTable as StageTable_
from .torappu.story_data import StoryData
from .torappu.story_review_group_client_data import StoryReviewGroupClientData
from .torappu.story_review_meta_table import StoryReviewMetaTable as StoryReviewMetaTable_
from .torappu.tip_table import TipTable as TipTable_
from .torappu.uni_equip_table import UniEquipTable as UniEquipTable_, UniEquipTableOld
from .torappu.zone_table import ZoneTable as ZoneTable_


class ActivityTable(ActivityTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class AudioTable(AudioData):
    __version__: str = "25-10-22-11-51-22_eda48a"


class BattleEquipTable(BaseStruct):
    equips: dict[str, BattleEquipPack]

    __version__: str = "25-10-22-11-51-22_eda48a"


class BuildingTable(BuildingData):
    __version__: str = "25-10-22-11-51-22_eda48a"


class CampaignTable(CampaignTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class ChapterTable(BaseStruct):
    chapters: dict[str, ChapterData]

    __version__: str = "25-10-22-11-51-22_eda48a"


class CharacterTable(BaseStruct):
    chars: dict[str, CharacterData]

    __version__: str = "25-10-22-11-51-22_eda48a"


class CharMasterTable(BaseStruct):
    masters: dict[str, MasterDataBundle]

    __version__: str = "25-10-22-11-51-22_eda48a"


class CharMetaTable(CharMetaTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class CharmTable(CharmData):
    __version__: str = "25-10-22-11-51-22_eda48a"


class CharPatchTable(CharPatchData):
    __version__: str = "25-10-22-11-51-22_eda48a"


class CharwordTable(CharwordTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class CheckinTable(CheckinTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class ClimbTowerTable(ClimbTowerTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class ClueTable(MeetingClueData):
    __version__: str = "25-10-22-11-51-22_eda48a"


class CrisisTable(CrisisTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class CrisisV2Table(CrisisV2SharedData):
    __version__: str = "25-10-22-11-51-22_eda48a"


class DisplayMetaTable(DisplayMetaData):
    __version__: str = "25-10-22-11-51-22_eda48a"


class EnemyHandbookTable(EnemyHandBookDataGroup):
    __version__: str = "25-10-22-11-51-22_eda48a"


class FavorTable(FavorTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class GachaTable(GachaData):
    __version__: str = "25-10-22-11-51-22_eda48a"


class GameDataConst(GameDataConsts):
    __version__: str = "25-10-22-11-51-22_eda48a"


class HandbookInfoTable(HandbookInfoTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class HandbookTable(HandbookTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class HandbookTeamTable(BaseStruct):
    team: dict[str, HandbookTeamData]

    __version__: str = "25-10-22-11-51-22_eda48a"


class ItemTable(ServerItemTable):
    __version__: str = "25-10-22-11-51-22_eda48a"


class MedalTable(MedalData):
    __version__: str = "25-10-22-11-51-22_eda48a"


class MissionTable(MissionTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class OpenServerTable(OpenServerSchedule):
    __version__: str = "25-10-22-11-51-22_eda48a"


class PlayerAvatarTable(PlayerAvatarData):
    __version__: str = "25-10-22-11-51-22_eda48a"


class RangeTable(BaseStruct):
    range: dict[str, RangeData]

    __version__: str = "25-10-22-11-51-22_eda48a"


class ReplicateTable(BaseStruct):
    replicate: dict[str, ReplicateTable_]

    __version__: str = "25-10-22-11-51-22_eda48a"


class RetroTable(RetroStageTable):
    __version__: str = "25-10-22-11-51-22_eda48a"


class RoguelikeTable(RoguelikeTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class RoguelikeTopicTable(RoguelikeTopicTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class SandboxPermTable(SandboxPermTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class SandboxTable(SandboxTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class ShopClientTable(ShopClientData):
    __version__: str = "25-10-22-11-51-22_eda48a"


class SkillTable(BaseStruct):
    skills: dict[str, SkillDataBundle]

    __version__: str = "25-10-22-11-51-22_eda48a"


class SkinTable(SkinTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class SpecialOperatorTable(SpecialOperatorTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class StageTable(StageTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class StoryReviewMetaTable(StoryReviewMetaTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class StoryReviewTable(BaseStruct):
    storyreview: dict[str, StoryReviewGroupClientData]

    __version__: str = "25-10-22-11-51-22_eda48a"


class StoryTable(BaseStruct):
    stories: dict[str, StoryData]

    __version__: str = "25-10-22-11-51-22_eda48a"


class TechBuffTable(BaseStruct):
    runes: list[RuneTable.PackedRuneData]

    __version__: str = "25-10-22-11-51-22_eda48a"


class TipTable(TipTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class TokenTable(BaseStruct):
    tokens: dict[str, TokenCharacterData]

    __version__: str = "25-10-22-11-51-22_eda48a"


class UniequipData(UniEquipTableOld):
    __version__: str = "25-10-22-11-51-22_eda48a"


class UniequipTable(UniEquipTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"


class ZoneTable(ZoneTable_):
    __version__: str = "25-10-22-11-51-22_eda48a"

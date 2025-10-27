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
    pass


class AudioTable(AudioData):
    pass


class BattleEquipTable(BaseStruct):
    equips: dict[str, BattleEquipPack]


class BuildingTable(BuildingData):
    pass


class CampaignTable(CampaignTable_):
    pass


class ChapterTable(BaseStruct):
    chapters: dict[str, ChapterData]


class CharacterTable(BaseStruct):
    chars: dict[str, CharacterData]


class CharMasterTable(BaseStruct):
    masters: dict[str, MasterDataBundle]


class CharMetaTable(CharMetaTable_):
    pass


class CharmTable(CharmData):
    pass


class CharPatchTable(CharPatchData):
    pass


class CharwordTable(CharwordTable_):
    pass


class CheckinTable(CheckinTable_):
    pass


class ClimbTowerTable(ClimbTowerTable_):
    pass


class ClueTable(MeetingClueData):
    pass


class CrisisTable(CrisisTable_):
    pass


class CrisisV2Table(CrisisV2SharedData):
    pass


class DisplayMetaTable(DisplayMetaData):
    pass


class EnemyHandbookTable(EnemyHandBookDataGroup):
    pass


class FavorTable(FavorTable_):
    pass


class GachaTable(GachaData):
    pass


class GameDataConst(GameDataConsts):
    pass


class HandbookInfoTable(HandbookInfoTable_):
    pass


class HandbookTable(HandbookTable_):
    pass


class HandbookTeamTable(BaseStruct):
    team: dict[str, HandbookTeamData]


class ItemTable(ServerItemTable):
    pass


class MedalTable(MedalData):
    pass


class MissionTable(MissionTable_):
    pass


class OpenServerTable(OpenServerSchedule):
    pass


class PlayerAvatarTable(PlayerAvatarData):
    pass


class RangeTable(BaseStruct):
    range: dict[str, RangeData]


class ReplicateTable(BaseStruct):
    replicate: dict[str, ReplicateTable_]


class RetroTable(RetroStageTable):
    pass


class RoguelikeTable(RoguelikeTable_):
    pass


class RoguelikeTopicTable(RoguelikeTopicTable_):
    pass


class SandboxPermTable(SandboxPermTable_):
    pass


class SandboxTable(SandboxTable_):
    pass


class ShopClientTable(ShopClientData):
    pass


class SkillTable(BaseStruct):
    skills: dict[str, SkillDataBundle]


class SkinTable(SkinTable_):
    pass


class SpecialOperatorTable(SpecialOperatorTable_):
    pass


class StageTable(StageTable_):
    pass


class StoryReviewMetaTable(StoryReviewMetaTable_):
    pass


class StoryReviewTable(BaseStruct):
    storyreview: dict[str, StoryReviewGroupClientData]


class StoryTable(BaseStruct):
    stories: dict[str, StoryData]


class TechBuffTable(BaseStruct):
    runes: list[RuneTable.PackedRuneData]


class TipTable(TipTable_):
    pass


class TokenTable(BaseStruct):
    tokens: dict[str, TokenCharacterData]


class UniequipData(UniEquipTableOld):
    pass


class UniequipTable(UniEquipTable_):
    pass


class ZoneTable(ZoneTable_):
    pass

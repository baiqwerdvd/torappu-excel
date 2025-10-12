import json
from pathlib import Path

from src.torappu_excel.models import (
    ActivityTable,
    AudioTable,
    BattleEquipTable,
    BuildingTable,
    CampaignTable,
    ChapterTable,
    CharMasterTable,
    CharMetaTable,
    CharPatchTable,
    CharacterTable,
    CharmTable,
    CharwordTable,
    CheckinTable,
    ClimbTowerTable,
    ClueTable,
    CrisisTable,
    CrisisV2Table,
    DisplayMetaTable,
    EnemyHandbookTable,
    FavorTable,
    GachaTable,
    GameDataConst,
    HandbookInfoTable,
    HandbookTable,
    HandbookTeamTable,
    ItemTable,
    MedalTable,
    MissionTable,
    OpenServerTable,
    PlayerAvatarTable,
    RangeTable,
    ReplicateTable,
    RetroTable,
    RoguelikeTable,
    RoguelikeTopicTable,
    SandboxPermTable,
    ShopClientTable,
    SkillTable,
    SkinTable,
    SpecialOperatorTable,
    StageTable,
    StoryReviewMetaTable,
    StoryReviewTable,
    StoryTable,
    TechBuffTable,
    TipTable,
    TokenTable,
    UniequipData,
    UniequipTable,
    ZoneTable,
)


async def test_client_table():
    base_path = Path("src/torappu_excel/json")

    activity_table(base_path)
    audio_table(base_path)
    battle_equip_table(base_path)
    building_table(base_path)
    campaign_table(base_path)
    chapter_table(base_path)
    char_master_table(base_path)
    char_meta_table(base_path)
    char_patch_table(base_path)
    character_table(base_path)
    charm_table(base_path)
    charword_table(base_path)
    checkin_table(base_path)
    climb_tower_table(base_path)
    clue_table(base_path)
    crisis_table(base_path)
    crisis_v2_table(base_path)
    display_meta_table(base_path)
    enemy_handbook_table(base_path)
    favor_table(base_path)
    gacha_table(base_path)
    game_data_const(base_path)
    handbook_info_table(base_path)
    handbook_table(base_path)
    handbook_team_table(base_path)
    item_table(base_path)
    medal_table(base_path)
    mission_table(base_path)
    open_server_table(base_path)
    player_avatar_table(base_path)
    range_table(base_path)
    replicate_table(base_path)
    retro_table(base_path)
    roguelike_table(base_path)
    roguelike_topic_table(base_path)
    sandbox_perm_table(base_path)
    shop_client_table(base_path)
    skill_table(base_path)
    skin_table(base_path)
    special_operator_table(base_path)
    stage_table(base_path)
    story_review_meta_table(base_path)
    story_review_table(base_path)
    story_table(base_path)
    tech_buff_table(base_path)
    tip_table(base_path)
    token_table(base_path)
    uniequip_data(base_path)
    uniequip_table(base_path)
    zone_table(base_path)


def activity_table(path: Path):
    with open(path / "activity_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ActivityTable.model_validate(data)


def audio_table(path: Path):
    with open(path / "audio_data.json", encoding="utf8") as f:
        data = json.load(f)
    _ = AudioTable.model_validate(data)


def battle_equip_table(path: Path):
    with open(path / "battle_equip_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = BattleEquipTable.model_validate({"equips": data})


def building_table(path: Path):
    with open(path / "building_data.json", encoding="utf8") as f:
        data = json.load(f)
    _ = BuildingTable.model_validate(data)


def campaign_table(path: Path):
    with open(path / "campaign_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CampaignTable.model_validate(data)


def chapter_table(path: Path):
    with open(path / "chapter_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ChapterTable.model_validate({"chapters": data})


def char_master_table(path: Path):
    with open(path / "char_master_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CharMasterTable.model_validate({"masters": data})


def char_meta_table(path: Path):
    with open(path / "char_meta_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CharMetaTable.model_validate(data)


def char_patch_table(path: Path):
    with open(path / "char_patch_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CharPatchTable.model_validate(data)


def character_table(path: Path):
    with open(path / "character_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CharacterTable.model_validate({"chars": data})


def charm_table(path: Path):
    with open(path / "charm_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CharmTable.model_validate(data)


def charword_table(path: Path):
    with open(path / "charword_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CharwordTable.model_validate(data)


def checkin_table(path: Path):
    with open(path / "checkin_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CheckinTable.model_validate(data)


def climb_tower_table(path: Path):
    with open(path / "climb_tower_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ClimbTowerTable.model_validate(data)


def clue_table(path: Path):
    with open(path / "clue_data.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ClueTable.model_validate(data)


def crisis_table(path: Path):
    with open(path / "crisis_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CrisisTable.model_validate(data)


def crisis_v2_table(path: Path):
    with open(path / "crisis_v2_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CrisisV2Table.model_validate(data)


def display_meta_table(path: Path):
    with open(path / "display_meta_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = DisplayMetaTable.model_validate(data)


def enemy_handbook_table(path: Path):
    with open(path / "enemy_handbook_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = EnemyHandbookTable.model_validate(data)


def favor_table(path: Path):
    with open(path / "favor_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = FavorTable.model_validate(data)


def gacha_table(path: Path):
    with open(path / "gacha_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = GachaTable.model_validate(data)


def game_data_const(path: Path):
    with open(path / "gamedata_const.json", encoding="utf8") as f:
        data = json.load(f)
    _ = GameDataConst.model_validate(data)


def handbook_info_table(path: Path):
    with open(path / "handbook_info_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = HandbookInfoTable.model_validate(data)


def handbook_table(path: Path):
    with open(path / "handbook_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = HandbookTable.model_validate(data)


def handbook_team_table(path: Path):
    with open(path / "handbook_team_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = HandbookTeamTable.model_validate({"team": data})


def item_table(path: Path):
    with open(path / "item_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ItemTable.model_validate(data)


def medal_table(path: Path):
    with open(path / "medal_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = MedalTable.model_validate(data)


def mission_table(path: Path):
    with open(path / "mission_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = MissionTable.model_validate(data)


def open_server_table(path: Path):
    with open(path / "open_server_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = OpenServerTable.model_validate(data)


def player_avatar_table(path: Path):
    with open(path / "player_avatar_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = PlayerAvatarTable.model_validate(data)


def range_table(path: Path):
    with open(path / "range_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = RangeTable.model_validate({"range": data})


def replicate_table(path: Path):
    with open(path / "replicate_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ReplicateTable.model_validate({"replicate": data})


def retro_table(path: Path):
    with open(path / "retro_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = RetroTable.model_validate(data)


def roguelike_table(path: Path):
    with open(path / "roguelike_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = RoguelikeTable.model_validate(data)


def roguelike_topic_table(path: Path):
    with open(path / "roguelike_topic_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = RoguelikeTopicTable.model_validate(data)


def sandbox_perm_table(path: Path):
    with open(path / "sandbox_perm_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = SandboxPermTable.model_validate(data)


def shop_client_table(path: Path):
    with open(path / "shop_client_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ShopClientTable.model_validate(data)


def skill_table(path: Path):
    with open(path / "skill_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = SkillTable.model_validate({"skills": data})


def skin_table(path: Path):
    with open(path / "skin_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = SkinTable.model_validate(data)


def special_operator_table(path: Path):
    with open(path / "special_operator_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = SpecialOperatorTable.model_validate(data)


def stage_table(path: Path):
    with open(path / "stage_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = StageTable.model_validate(data)


def story_review_meta_table(path: Path):
    with open(path / "story_review_meta_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = StoryReviewMetaTable.model_validate(data)


def story_review_table(path: Path):
    with open(path / "story_review_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = StoryReviewTable.model_validate({"storyreview": data})


def story_table(path: Path):
    with open(path / "story_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = StoryTable.model_validate({"stories": data})


def tech_buff_table(path: Path):
    with open(path / "tech_buff_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = TechBuffTable.model_validate(data)


def tip_table(path: Path):
    with open(path / "tip_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = TipTable.model_validate(data)


def token_table(path: Path):
    with open(path / "token_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = TokenTable.model_validate({"tokens": data})


def uniequip_data(path: Path):
    with open(path / "uniequip_data.json", encoding="utf8") as f:
        data = json.load(f)
    _ = UniequipData.model_validate(data)


def uniequip_table(path: Path):
    with open(path / "uniequip_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = UniequipTable.model_validate(data)


def zone_table(path: Path):
    with open(path / "zone_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ZoneTable.model_validate(data)

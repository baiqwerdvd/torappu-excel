import json
from pathlib import Path

from src.torappu_excel.models import (
    ActivityTable,
    AudioTable,
    BattleEquipTable,
    BuildingTable,
    CampaignTable,
    ChapterTable,
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
    _ = ActivityTable.convert(data)


def audio_table(path: Path):
    with open(path / "audio_data.json", encoding="utf8") as f:
        data = json.load(f)
    _ = AudioTable.convert(data)


def battle_equip_table(path: Path):
    with open(path / "battle_equip_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = BattleEquipTable.convert({"equips": data})


def building_table(path: Path):
    with open(path / "building_data.json", encoding="utf8") as f:
        data = json.load(f)
    _ = BuildingTable.convert(data)


def campaign_table(path: Path):
    with open(path / "campaign_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CampaignTable.convert(data)


def chapter_table(path: Path):
    with open(path / "chapter_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ChapterTable.convert({"chapters": data})


def char_meta_table(path: Path):
    with open(path / "char_meta_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CharMetaTable.convert(data)


def char_patch_table(path: Path):
    with open(path / "char_patch_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CharPatchTable.convert(data)


def character_table(path: Path):
    with open(path / "character_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CharacterTable.convert({"chars": data})


def charm_table(path: Path):
    with open(path / "charm_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CharmTable.convert(data)


def charword_table(path: Path):
    with open(path / "charword_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CharwordTable.convert(data)


def checkin_table(path: Path):
    with open(path / "checkin_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CheckinTable.convert(data)


def climb_tower_table(path: Path):
    with open(path / "climb_tower_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ClimbTowerTable.convert(data)


def clue_table(path: Path):
    with open(path / "clue_data.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ClueTable.convert(data)


def crisis_table(path: Path):
    with open(path / "crisis_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CrisisTable.convert(data)


def crisis_v2_table(path: Path):
    with open(path / "crisis_v2_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = CrisisV2Table.convert(data)


def display_meta_table(path: Path):
    with open(path / "display_meta_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = DisplayMetaTable.convert(data)


def enemy_handbook_table(path: Path):
    with open(path / "enemy_handbook_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = EnemyHandbookTable.convert(data)


def favor_table(path: Path):
    with open(path / "favor_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = FavorTable.convert(data)


def gacha_table(path: Path):
    with open(path / "gacha_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = GachaTable.convert(data)


def game_data_const(path: Path):
    with open(path / "gamedata_const.json", encoding="utf8") as f:
        data = json.load(f)
    _ = GameDataConst.convert(data)


def handbook_info_table(path: Path):
    with open(path / "handbook_info_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = HandbookInfoTable.convert(data)


def handbook_table(path: Path):
    with open(path / "handbook_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = HandbookTable.convert(data)


def handbook_team_table(path: Path):
    with open(path / "handbook_team_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = HandbookTeamTable.convert({"team": data})


def item_table(path: Path):
    with open(path / "item_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ItemTable.convert(data)


def medal_table(path: Path):
    with open(path / "medal_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = MedalTable.convert(data)


def mission_table(path: Path):
    with open(path / "mission_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = MissionTable.convert(data)


def open_server_table(path: Path):
    with open(path / "open_server_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = OpenServerTable.convert(data)


def player_avatar_table(path: Path):
    with open(path / "player_avatar_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = PlayerAvatarTable.convert(data)


def range_table(path: Path):
    with open(path / "range_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = RangeTable.convert({"range": data})


def replicate_table(path: Path):
    with open(path / "replicate_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ReplicateTable.convert({"replicate": data})


def retro_table(path: Path):
    with open(path / "retro_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = RetroTable.convert(data)


def roguelike_table(path: Path):
    with open(path / "roguelike_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = RoguelikeTable.convert(data)


def roguelike_topic_table(path: Path):
    with open(path / "roguelike_topic_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = RoguelikeTopicTable.convert(data)


def sandbox_perm_table(path: Path):
    with open(path / "sandbox_perm_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = SandboxPermTable.convert(data)


def shop_client_table(path: Path):
    with open(path / "shop_client_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ShopClientTable.convert(data)


def skill_table(path: Path):
    with open(path / "skill_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = SkillTable.convert({"skills": data})


def skin_table(path: Path):
    with open(path / "skin_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = SkinTable.convert(data)


def stage_table(path: Path):
    with open(path / "stage_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = StageTable.convert(data)


def story_review_meta_table(path: Path):
    with open(path / "story_review_meta_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = StoryReviewMetaTable.convert(data)


def story_review_table(path: Path):
    with open(path / "story_review_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = StoryReviewTable.convert({"storyreview": data})


def story_table(path: Path):
    with open(path / "story_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = StoryTable.convert({"stories": data})


def tech_buff_table(path: Path):
    with open(path / "tech_buff_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = TechBuffTable.convert(data)


def tip_table(path: Path):
    with open(path / "tip_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = TipTable.convert(data)


def token_table(path: Path):
    with open(path / "token_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = TokenTable.convert({"tokens": data})


def uniequip_data(path: Path):
    with open(path / "uniequip_data.json", encoding="utf8") as f:
        data = json.load(f)
    _ = UniequipData.convert(data)


def uniequip_table(path: Path):
    with open(path / "uniequip_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = UniequipTable.convert(data)


def zone_table(path: Path):
    with open(path / "zone_table.json", encoding="utf8") as f:
        data = json.load(f)
    _ = ZoneTable.convert(data)

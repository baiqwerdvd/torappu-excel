import asyncio

from .models import (
    ActivityTable,
    AudioData,
    BattleEquipTable,
    BuildingData,
    CampaignTable,
    ChapterTable,
    CharMetaTable,
    CharPatchTable,
    CharacterTable,
    CharmTable,
    CharwordTable,
    CheckinTable,
    ClimbTowerTable,
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
    MeetingClueData,
    MissionTable,
    OpenServerTable,
    PlayerAvatarTable,
    RangeTable,
    ReplicateTable,
    RetroTable,
    RoguelikeTable,
    RoguelikeTopicTable,
    SandboxPermTable,
    SandboxTable,
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
from .utils import is_valid_async_func, read_json


class ExcelTableManager:
    activity_table_: ActivityTable | None = None
    audio_data_: AudioData | None = None
    battle_equip_table_: BattleEquipTable | None = None
    building_data_: BuildingData | None = None
    campaign_table_: CampaignTable | None = None
    chapter_table_: ChapterTable | None = None
    character_table_: CharacterTable | None = None
    char_meta_table_: CharMetaTable | None = None
    charm_table_: CharmTable | None = None
    char_patch_table_: CharPatchTable | None = None
    charword_table_: CharwordTable | None = None
    checkin_table_: CheckinTable | None = None
    climb_tower_table_: ClimbTowerTable | None = None
    clue_data_: MeetingClueData | None = None
    crisis_table_: CrisisTable | None = None
    crisis_v2_table_: CrisisV2Table | None = None
    display_meta_table_: DisplayMetaTable | None = None
    enemy_handbook_table_: EnemyHandbookTable | None = None
    favor_table_: FavorTable | None = None
    gacha_table_: GachaTable | None = None
    gamedata_const_: GameDataConst | None = None
    handbook_info_table_: HandbookInfoTable | None = None
    handbook_table_: HandbookTable | None = None
    handbook_team_table_: HandbookTeamTable | None = None
    item_table_: ItemTable | None = None
    medal_table_: MedalTable | None = None
    mission_table_: MissionTable | None = None
    open_server_table_: OpenServerTable | None = None
    player_avatar_table_: PlayerAvatarTable | None = None
    range_table_: RangeTable | None = None
    replicate_table_: ReplicateTable | None = None
    retro_table_: RetroTable | None = None
    roguelike_table_: RoguelikeTable | None = None
    roguelike_topic_table_: RoguelikeTopicTable | None = None
    sandbox_table_: SandboxTable | None = None
    sandbox_perm_table_: SandboxPermTable | None = None
    shop_client_table_: ShopClientTable | None = None
    skill_table_: SkillTable | None = None
    skin_table_: SkinTable | None = None
    stage_table_: StageTable | None = None
    story_review_meta_table_: StoryReviewMetaTable | None = None
    story_review_table_: StoryReviewTable | None = None
    story_table_: StoryTable | None = None
    tech_buff_table_: TechBuffTable | None = None
    tip_table_: TipTable | None = None
    token_table_: TokenTable | None = None
    uniequip_data_: UniequipData | None = None
    uniequip_table_: UniequipTable | None = None
    zone_table_: ZoneTable | None = None

    async def activity_table(self) -> None:
        self.activity_table_ = ActivityTable.convert(read_json("activity_table.json"))

    @property
    def ACTIVITY_TABLE(self) -> ActivityTable:
        if self.activity_table_ is None:
            raise ValueError("activity_table is not loaded")
        return self.activity_table_

    async def audio_data(self) -> None:
        self.audio_data_ = AudioData.convert(read_json("audio_data.json"))

    @property
    def AUDIO_DATA(self) -> AudioData:
        if self.audio_data_ is None:
            raise ValueError("audio_data is not loaded")
        return self.audio_data_

    async def battle_equip_table(self) -> None:
        self.battle_equip_table_ = BattleEquipTable.convert({"equips": read_json("battle_equip_table.json")})

    @property
    def BATTLE_EQUIP_TABLE(self) -> BattleEquipTable:
        if self.battle_equip_table_ is None:
            raise ValueError("battle_equip_table is not loaded")
        return self.battle_equip_table_

    async def building_data(self) -> None:
        self.building_data_ = BuildingData.convert(read_json("building_data.json"))

    @property
    def BUILDING_DATA(self) -> BuildingData:
        if self.building_data_ is None:
            raise ValueError("building_data is not loaded")
        return self.building_data_

    async def campaign_table(self) -> None:
        self.campaign_table_ = CampaignTable.convert(read_json("campaign_table.json"))

    @property
    def CAMPAIGN_TABLE(self) -> CampaignTable:
        if self.campaign_table_ is None:
            raise ValueError("campaign_table is not loaded")
        return self.campaign_table_

    async def chapter_table(self) -> None:
        self.chapter_table_ = ChapterTable.convert({"chapters": read_json("chapter_table.json")})

    @property
    def CHAPTER_TABLE(self) -> ChapterTable:
        if self.chapter_table_ is None:
            raise ValueError("chapter_table is not loaded")
        return self.chapter_table_

    async def character_table(self) -> None:
        self.character_table_ = CharacterTable.convert({"chars": read_json("character_table.json")})

    @property
    def CHARATER_TABLE(self) -> CharacterTable:
        if self.character_table_ is None:
            raise ValueError("character_table is not loaded")
        return self.character_table_

    async def char_meta_table(self) -> None:
        self.char_meta_table_ = CharMetaTable.convert(read_json("char_meta_table.json"))

    @property
    def CHAR_META_TABLE(self) -> CharMetaTable:
        if self.char_meta_table_ is None:
            raise ValueError("char_meta_table is not loaded")
        return self.char_meta_table_

    async def charm_table(self) -> None:
        self.charm_table_ = CharmTable.convert(read_json("charm_table.json"))

    @property
    def CHARM_TABLE(self) -> CharmTable:
        if self.charm_table_ is None:
            raise ValueError("charm_table is not loaded")
        return self.charm_table_

    async def char_patch_table(self) -> None:
        self.char_patch_table_ = CharPatchTable.convert(read_json("char_patch_table.json"))

    @property
    def CHAR_PATCH_TABLE(self) -> CharPatchTable:
        if self.char_patch_table_ is None:
            raise ValueError("char_patch_table is not loaded")
        return self.char_patch_table_

    async def charword_table(self) -> None:
        self.charword_table_ = CharwordTable.convert(read_json("charword_table.json"))

    @property
    def CHARWORD_TABLE(self) -> CharwordTable:
        if self.charword_table_ is None:
            raise ValueError("charword_table is not loaded")
        return self.charword_table_

    async def checkin_table(self) -> None:
        self.checkin_table_ = CheckinTable.convert(read_json("checkin_table.json"))

    @property
    def CHECKIN_TABLE(self) -> CheckinTable:
        if self.checkin_table_ is None:
            raise ValueError("checkin_table is not loaded")
        return self.checkin_table_

    async def climb_tower_table(self) -> None:
        self.climb_tower_table_ = ClimbTowerTable.convert(read_json("climb_tower_table.json"))

    @property
    def CLIMB_TOWER_TABLE(self) -> ClimbTowerTable:
        if self.climb_tower_table_ is None:
            raise ValueError("climb_tower_table is not loaded")
        return self.climb_tower_table_

    async def clue_data(self) -> None:
        self.clue_data_ = MeetingClueData.convert(read_json("clue_data.json"))

    @property
    def CLUE_DATA(self) -> MeetingClueData:
        if self.clue_data_ is None:
            raise ValueError("clue_data is not loaded")
        return self.clue_data_

    async def crisis_table(self) -> None:
        self.crisis_table_ = CrisisTable.convert(read_json("crisis_table.json"))

    @property
    def CRISIS_TABLE(self) -> CrisisTable:
        if self.crisis_table_ is None:
            raise ValueError("crisis_table is not loaded")
        return self.crisis_table_

    async def crisis_v2_table(self) -> None:
        self.crisis_v2_table_ = CrisisV2Table.convert(read_json("crisis_v2_table.json"))

    @property
    def CRISIS_V2_TABLE(self) -> CrisisV2Table:
        if self.crisis_v2_table_ is None:
            raise ValueError("crisis_v2_table is not loaded")
        return self.crisis_v2_table_

    async def display_meta_table(self) -> None:
        self.display_meta_table_ = DisplayMetaTable.convert(read_json("display_meta_table.json"))

    @property
    def DISPLAY_META_TABLE(self) -> DisplayMetaTable:
        if self.display_meta_table_ is None:
            raise ValueError("display_meta_table is not loaded")
        return self.display_meta_table_

    async def enemy_handbook_table(self) -> None:
        self.enemy_handbook_table_ = EnemyHandbookTable.convert(read_json("enemy_handbook_table.json"))

    @property
    def ENEMY_HANDBOOK_TABLE(self) -> EnemyHandbookTable:
        if self.enemy_handbook_table_ is None:
            raise ValueError("enemy_handbook_table is not loaded")
        return self.enemy_handbook_table_

    async def favor_table(self) -> None:
        self.favor_table_ = FavorTable.convert(read_json("favor_table.json"))

    @property
    def FAVOR_TABLE(self) -> FavorTable:
        if self.favor_table_ is None:
            raise ValueError("favor_table is not loaded")
        return self.favor_table_

    async def gacha_table(self) -> None:
        self.gacha_table_ = GachaTable.convert(read_json("gacha_table.json"))

    @property
    def GACHA_TABLE(self) -> GachaTable:
        if self.gacha_table_ is None:
            raise ValueError("gacha_table is not loaded")
        return self.gacha_table_

    async def gamedata_const(self) -> None:
        self.gamedata_const_ = GameDataConst.convert(read_json("gamedata_const.json"))

    @property
    def GAMEDATA_CONST(self) -> GameDataConst:
        if self.gamedata_const_ is None:
            raise ValueError("gamedata_const is not loaded")
        return self.gamedata_const_

    async def handbook_info_table(self) -> None:
        self.handbook_info_table_ = HandbookInfoTable.convert(read_json("handbook_info_table.json"))

    @property
    def HANDBOOK_INFO_TABLE(self) -> HandbookInfoTable:
        if self.handbook_info_table_ is None:
            raise ValueError("handbook_info_table is not loaded")
        return self.handbook_info_table_

    async def handbook_table(self) -> None:
        self.handbook_table_ = HandbookTable.convert(read_json("handbook_table.json"))

    @property
    def HANDBOOK_TABLE(self) -> HandbookTable:
        if self.handbook_table_ is None:
            raise ValueError("handbook_table is not loaded")
        return self.handbook_table_

    async def handbook_team_table(self) -> None:
        self.handbook_team_table_ = HandbookTeamTable.convert({"team": read_json("handbook_team_table.json")})

    @property
    def HANDBOOK_TEAM_TABLE(self) -> HandbookTeamTable:
        if self.handbook_team_table_ is None:
            raise ValueError("handbook_team_table is not loaded")
        return self.handbook_team_table_

    async def item_table(self) -> None:
        self.item_table_ = ItemTable.convert(read_json("item_table.json"))

    @property
    def ITEM_TABLE(self) -> ItemTable:
        if self.item_table_ is None:
            raise ValueError("item_table is not loaded")
        return self.item_table_

    async def medal_table(self) -> None:
        self.medal_table_ = MedalTable.convert(read_json("medal_table.json"))

    @property
    def MEDAL_TABLE(self) -> MedalTable:
        if self.medal_table_ is None:
            raise ValueError("medal_table is not loaded")
        return self.medal_table_

    async def mission_table(self) -> None:
        self.mission_table_ = MissionTable.convert(read_json("mission_table.json"))

    @property
    def MISSION_TABLE(self) -> MissionTable:
        if self.mission_table_ is None:
            raise ValueError("mission_table is not loaded")
        return self.mission_table_

    async def open_server_table(self) -> None:
        self.open_server_table_ = OpenServerTable.convert(read_json("open_server_table.json"))

    @property
    def OPEN_SERVER_TABLE(self) -> OpenServerTable:
        if self.open_server_table_ is None:
            raise ValueError("open_server_table is not loaded")
        return self.open_server_table_

    async def player_avatar_table(self) -> None:
        self.player_avatar_table_ = PlayerAvatarTable.convert(read_json("player_avatar_table.json"))

    @property
    def PLAYER_AVATAR_TABLE(self) -> PlayerAvatarTable:
        if self.player_avatar_table_ is None:
            raise ValueError("player_avatar_table is not loaded")
        return self.player_avatar_table_

    async def range_table(self) -> None:
        self.range_table_ = RangeTable.convert({"range": read_json("range_table.json")})

    @property
    def RANGE_TABLE(self) -> RangeTable:
        if self.range_table_ is None:
            raise ValueError("range_table is not loaded")
        return self.range_table_

    async def replicate_table(self) -> None:
        self.replicate_table_ = ReplicateTable.convert({"replicate": read_json("replicate_table.json")})

    @property
    def REPLICATE_TABLE(self) -> ReplicateTable:
        if self.replicate_table_ is None:
            raise ValueError("replicate_table is not loaded")
        return self.replicate_table_

    async def retro_table(self) -> None:
        self.retro_table_ = RetroTable.convert(read_json("retro_table.json"))

    @property
    def RETRO_TABLE(self) -> RetroTable:
        if self.retro_table_ is None:
            raise ValueError("retro_table is not loaded")
        return self.retro_table_

    async def roguelike_table(self) -> None:
        self.roguelike_table_ = RoguelikeTable.convert(read_json("roguelike_table.json"))

    @property
    def ROGUELIKE_TABLE(self) -> RoguelikeTable:
        if self.roguelike_table_ is None:
            raise ValueError("roguelike_table is not loaded")
        return self.roguelike_table_

    async def roguelike_topic_table(self) -> None:
        self.roguelike_topic_table_ = RoguelikeTopicTable.convert(read_json("roguelike_topic_table.json"))

    @property
    def ROGUELIKE_TOPIC_TABLE(self) -> RoguelikeTopicTable:
        if self.roguelike_topic_table_ is None:
            raise ValueError("roguelike_topic_table is not loaded")
        return self.roguelike_topic_table_

    async def sandbox_table(self) -> None:
        try:
            self.sandbox_table_ = SandboxTable.convert(read_json("sandbox_table.json"))
        except FileNotFoundError as _:
            self.sandbox_table_ = None

    @property
    def SANDBOX_TABLE(self) -> SandboxTable:
        if self.sandbox_table_ is None:
            raise ValueError("sandbox_table is not loaded")
        return self.sandbox_table_

    async def sandbox_perm_table(self) -> None:
        self.sandbox_perm_table_ = SandboxPermTable.convert(read_json("sandbox_perm_table.json"))

    @property
    def SANDBOX_PERM_TABLE(self) -> SandboxPermTable:
        if self.sandbox_perm_table_ is None:
            raise ValueError("sandbox_perm_table is not loaded")
        return self.sandbox_perm_table_

    async def shop_client_table(self) -> None:
        self.shop_client_table_ = ShopClientTable.convert(read_json("shop_client_table.json"))

    @property
    def SHOP_CLIENT_TABLE(self) -> ShopClientTable:
        if self.shop_client_table_ is None:
            raise ValueError("shop_client_table is not loaded")
        return self.shop_client_table_

    async def skill_table(self) -> None:
        self.skill_table_ = SkillTable.convert({"skills": read_json("skill_table.json")})

    @property
    def SKILL_TABLE(self) -> SkillTable:
        if self.skill_table_ is None:
            raise ValueError("skill_table is not loaded")
        return self.skill_table_

    async def skin_table(self) -> None:
        self.skin_table_ = SkinTable.convert(read_json("skin_table.json"))

    @property
    def SKIN_TABLE(self) -> SkinTable:
        if self.skin_table_ is None:
            raise ValueError("skin_table is not loaded")
        return self.skin_table_

    async def stage_table(self) -> None:
        self.stage_table_ = StageTable.convert(read_json("stage_table.json"))

    @property
    def STAGE_TABLE(self) -> StageTable:
        if self.stage_table_ is None:
            raise ValueError("stage_table is not loaded")
        return self.stage_table_

    async def story_review_meta_table(self) -> None:
        self.story_review_meta_table_ = StoryReviewMetaTable.convert(read_json("story_review_meta_table.json"))

    @property
    def STORY_REVIEW_META_TABLE(self) -> StoryReviewMetaTable:
        if self.story_review_meta_table_ is None:
            raise ValueError("story_review_meta_table is not loaded")
        return self.story_review_meta_table_

    async def story_review_table(self) -> None:
        self.story_review_table_ = StoryReviewTable.convert({"storyreview": read_json("story_review_table.json")})

    @property
    def STORY_REVIEW_TABLE(self) -> StoryReviewTable:
        if self.story_review_table_ is None:
            raise ValueError("story_review_table is not loaded")
        return self.story_review_table_

    async def story_table(self) -> None:
        self.story_table_ = StoryTable.convert({"stories": read_json("story_table.json")})

    @property
    def STORY_TABLE(self) -> StoryTable:
        if self.story_table_ is None:
            raise ValueError("story_table is not loaded")
        return self.story_table_

    async def tech_buff_table(self) -> None:
        self.tech_buff_table_ = TechBuffTable.convert(read_json("tech_buff_table.json"))

    @property
    def TECH_BUFF_TABLE(self) -> TechBuffTable:
        if self.tech_buff_table_ is None:
            raise ValueError("tech_buff_table is not loaded")
        return self.tech_buff_table_

    async def tip_table(self) -> None:
        self.tip_table_ = TipTable.convert(read_json("tip_table.json"))

    @property
    def TIP_TABLE(self) -> TipTable:
        if self.tip_table_ is None:
            raise ValueError("tip_table is not loaded")
        return self.tip_table_

    async def token_table(self) -> None:
        self.token_table_ = TokenTable.convert({"tokens": read_json("token_table.json")})

    @property
    def TOKEN_TABLE(self) -> TokenTable:
        if self.token_table_ is None:
            raise ValueError("token_table is not loaded")
        return self.token_table_

    async def uniequip_data(self) -> None:
        self.uniequip_data_ = UniequipData.convert(read_json("uniequip_data.json"))

    @property
    def UNIEQUIP_DATA(self) -> UniequipData:
        if self.uniequip_data_ is None:
            raise ValueError("uniequip_data is not loaded")
        return self.uniequip_data_

    async def uniequip_table(self) -> None:
        self.uniequip_table_ = UniequipTable.convert(read_json("uniequip_table.json"))

    @property
    def UNIEQUIP_TABLE(self) -> UniequipTable:
        if self.uniequip_table_ is None:
            raise ValueError("uniequip_table is not loaded")
        return self.uniequip_table_

    async def zone_table(self) -> None:
        self.zone_table_ = ZoneTable.convert(read_json("zone_table.json"))

    @property
    def ZONE_TABLE(self) -> ZoneTable:
        if self.zone_table_ is None:
            raise ValueError("zone_table is not loaded")
        return self.zone_table_

    async def preload_table(self) -> None:
        async with asyncio.TaskGroup() as group:
            for name in dir(self):
                try:
                    method = getattr(self, name)
                except ValueError:
                    continue

                if is_valid_async_func(method, ["preload_table"]):
                    _task = group.create_task(method())

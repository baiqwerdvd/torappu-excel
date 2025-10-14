from pydantic import BaseModel, ConfigDict

from .charm_status import CharmStatus
from .mission_player_data import MissionPlayerData
from .player_activity import PlayerActivity
from .player_april_fool import PlayerAprilFool
from .player_avatar import PlayerAvatar
from .player_building import PlayerBuilding
from .player_campaign import PlayerCampaign
from .player_carousel import PlayerCarousel
from .player_cart_info import PlayerCartInfo
from .player_char_rotation import PlayerCharRotation
from .player_check_in import PlayerCheckIn
from .player_collection import PlayerCollection
from .player_consumable_item import PlayerConsumableItem
from .player_crisis import PlayerCrisis
from .player_crisis_v2 import PlayerCrisisV2
from .player_cross_app_share import PlayerCrossAppShare
from .player_deep_sea import PlayerDeepSea
from .player_dex_nav import PlayerDexNav
from .player_dungeon import PlayerDungeon
from .player_emoticon import PlayerEmoticon
from .player_equipment import PlayerEquipment
from .player_events import PlayerEvents
from .player_firework import PlayerFirework
from .player_gacha import PlayerGacha
from .player_home_background import PlayerHomeBackground
from .player_home_theme import PlayerHomeTheme
from .player_invite_data import PlayerInviteData
from .player_limited_drop_buff import PlayerLimitedDropBuff
from .player_mainline_record import PlayerMainlineRecord
from .player_medal import PlayerMedal
from .player_meta import PlayerMeta
from .player_monthly_sub_per import PlayerMonthlySubPer
from .player_name_card_style import PlayerNameCardStyle
from .player_npc_with_audio import PlayerNpcWithAudio
from .player_open_server import PlayerOpenServer
from .player_performance_story import PlayerPerformanceStory
from .player_push_flags import PlayerPushFlags
from .player_recal_rune import PlayerRecalRune
from .player_recruit import PlayerRecruit
from .player_retro import PlayerRetro
from .player_return_data import PlayerReturnData
from .player_roguelike import PlayerRoguelike
from .player_roguelike_v2 import PlayerRoguelikeV2
from .player_sandbox_perm import PlayerSandboxPerm
from .player_setting import PlayerSetting
from .player_shop import PlayerShop
from .player_siracusa_map import PlayerSiracusaMap
from .player_skins import PlayerSkins
from .player_social import PlayerSocial
from .player_status import PlayerStatus
from .player_story_review import PlayerStoryReview
from .player_template_shop import PlayerTemplateShop
from .player_template_trap import PlayerTemplateTrap
from .player_ticket_item import PlayerTicketItem
from .player_tower import PlayerTower
from .player_training_camp import PlayerTrainingCamp
from .player_troop import PlayerTroop


class PlayerDataModel(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    event: PlayerEvents
    pushFlags: PlayerPushFlags
    status: PlayerStatus
    monthlySub: dict[str, PlayerMonthlySubPer] | None = None
    troop: PlayerTroop
    dungeon: PlayerDungeon
    checkIn: PlayerCheckIn
    openServer: PlayerOpenServer
    activity: PlayerActivity
    templateTrap: PlayerTemplateTrap
    retro: PlayerRetro
    dexNav: PlayerDexNav
    skin: PlayerSkins
    medal: PlayerMedal
    avatar: PlayerAvatar
    collectionReward: PlayerCollection
    equipment: PlayerEquipment
    inventory: dict[str, int]
    consumable: dict[str, dict[int, PlayerConsumableItem]]
    ticket: dict[str, PlayerTicketItem]
    shop: PlayerShop
    invite: dict[str, dict[str, PlayerInviteData]]
    tshop: dict[str, PlayerTemplateShop]
    recruit: PlayerRecruit
    carousel: PlayerCarousel
    gacha: PlayerGacha
    social: PlayerSocial
    mission: MissionPlayerData
    building: PlayerBuilding
    crisis: PlayerCrisis
    crisisV2: PlayerCrisisV2
    recalRune: PlayerRecalRune
    storyreview: PlayerStoryReview
    roguelike: PlayerRoguelike
    rlv2: PlayerRoguelikeV2
    backflow: PlayerReturnData
    campaignsV2: PlayerCampaign
    charm: CharmStatus
    deepSea: PlayerDeepSea
    car: PlayerCartInfo
    tower: PlayerTower
    siracusaMap: PlayerSiracusaMap
    firework: PlayerFirework
    sandboxPerm: PlayerSandboxPerm
    emoticon: PlayerEmoticon
    share: PlayerCrossAppShare
    trainingGround: PlayerTrainingCamp
    background: PlayerHomeBackground
    homeTheme: PlayerHomeTheme
    nameCardStyle: PlayerNameCardStyle
    setting: PlayerSetting
    aprilFool: PlayerAprilFool
    npcAudio: dict[str, PlayerNpcWithAudio]
    charRotation: PlayerCharRotation
    mainline: PlayerMainlineRecord
    limitedBuff: PlayerLimitedDropBuff
    performanceStory: PlayerPerformanceStory
    checkMeta: PlayerMeta

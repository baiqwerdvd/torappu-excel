from .avatar_info import AvatarInfo
from .player_birthday import PlayerBirthday
from .player_friend_assist import PlayerFriendAssist
from .voice_lang_type import VoiceLangType
from ..common import BaseStruct


class PlayerStatus(BaseStruct):
    nickName: str
    nickNumber: str
    serverName: str
    ap: int
    lastApAddTime: int
    lastRefreshTs: int
    lastOnlineTs: int
    level: int
    exp: int
    maxAp: int
    practiceTicket: int
    gold: int
    diamondShard: int
    recruitLicense: int
    gachaTicket: int
    tenGachaTicket: int
    instantFinishTicket: int
    hggShard: int
    lggShard: int
    classicShard: int
    socialPoint: int
    buyApRemainTimes: int
    apLimitUpFlag: int
    uid: str
    classicGachaTicket: int
    classicTenGachaTicket: int
    registerTs: int
    secretary: str
    secretarySkinId: str
    resume: str
    birthday: PlayerBirthday
    monthlySubscriptionEndTime: int
    monthlySubscriptionStartTime: int
    tipMonthlyCardExpireTs: int
    progress: int
    mainStageProgress: str | None
    avatarId: str
    avatar: AvatarInfo
    globalVoiceLan: VoiceLangType
    iosDiamond: int
    androidDiamond: int
    flags: dict[str, int]
    friendNumLimit: int
    payDiamond: int | None = None
    freeDiamond: int | None = None
    secretarySkinSp: bool | None = None
    friendAssist: list[PlayerFriendAssist] | None = None

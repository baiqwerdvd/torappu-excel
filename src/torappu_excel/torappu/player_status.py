from pydantic import BaseModel, ConfigDict

from .avatar_info import AvatarInfo
from .player_birthday import PlayerBirthday
from .player_friend_assist import PlayerFriendAssist
from .voice_lang_type import VoiceLangType


class PlayerStatus(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
    apLimitUpFlag: bool
    uid: str
    classicGachaTicket: int
    classicTenGachaTicket: int
    registerTs: int
    secretary: str
    secretarySkinId: str
    secretarySkinSp: bool | None = None
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
    payDiamond: int | None = None
    freeDiamond: int | None = None
    flags: dict[str, bool]
    friendNumLimit: int
    friendAssist: list[PlayerFriendAssist] | None = None

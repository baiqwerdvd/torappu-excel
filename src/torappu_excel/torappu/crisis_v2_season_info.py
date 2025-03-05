from ..common import BaseStruct

from msgspec import field


class CrisisV2SeasonInfo(BaseStruct):
    seasonId: str
    name: str
    startTs: int
    endTs: int
    medalGroupId: str
    medalId: str
    themeColor1: str
    themeColor2: str
    themeColor3: str
    seasonBgm: str
    seasonBgmChallenge: str
    crisisV2SeasonCode: str
    textColor: str | None = field(default=None)
    backColor: str | None = field(default=None)

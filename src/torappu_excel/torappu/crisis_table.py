from .item_bundle import ItemBundle
from ..common import BaseStruct

from msgspec import field


class StringKeyFrames(BaseStruct):
    level: int
    data: str


class CrisisClientDataSeasonInfo(BaseStruct):
    seasonId: str
    startTs: int
    endTs: int
    name: str
    crisisRuneCoinUnlockItem: ItemBundle
    permBgm: str
    medalGroupId: str | None
    bgmHardPoint: int
    permBgmHard: str | None


class CrisisMapRankInfo(BaseStruct):
    rewards: list[ItemBundle]
    unlockPoint: int


class CrisisTable(BaseStruct):
    seasonInfo: list[CrisisClientDataSeasonInfo]
    meta: str
    unlockCoinLv3: int
    hardPointPerm: int
    hardPointTemp: int
    voiceGrade: int
    crisisRuneCoinUnlockItemTitle: str
    crisisRuneCoinUnlockItemDesc: str
    tempAppraise: list[StringKeyFrames] = field(default_factory=list)
    permAppraise: list[StringKeyFrames] = field(default_factory=list)
    mapRankInfo: dict[str, CrisisMapRankInfo] = field(default_factory=dict)

from dataclasses import field

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class StringKeyFrames(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    level: int
    data: str


class CrisisClientDataSeasonInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    seasonId: str
    startTs: int
    endTs: int
    name: str
    crisisRuneCoinUnlockItem: ItemBundle
    permBgm: str
    medalGroupId: str | None
    bgmHardPoint: int
    permBgmHard: str | None


class CrisisMapRankInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rewards: list[ItemBundle]
    unlockPoint: int


class CrisisTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    seasonInfo: list[CrisisClientDataSeasonInfo]
    meta: str
    unlockCoinLv3: int
    hardPointPerm: int
    hardPointTemp: int
    voiceGrade: int
    crisisRuneCoinUnlockItemTitle: str
    crisisRuneCoinUnlockItemDesc: str
    tempAppraise: list[StringKeyFrames] = field(default_factory=list[StringKeyFrames])
    permAppraise: list[StringKeyFrames] = field(default_factory=list[StringKeyFrames])
    mapRankInfo: dict[str, CrisisMapRankInfo] = field(default_factory=dict[str, CrisisMapRankInfo])

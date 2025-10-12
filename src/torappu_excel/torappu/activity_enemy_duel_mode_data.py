from pydantic import BaseModel, ConfigDict

from .enemy_duel_mode_type import EnemyDuelModeType


class ActivityEnemyDuelModeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    modeId: str
    isMultiPlayer: bool
    isRoom: bool
    modeType: EnemyDuelModeType
    stageIds: list[str]
    pageId: int
    innerSortId: int
    modeName: str
    modeShortName: str
    modeEnName: str
    maxPlayer: int
    preposedMode: str | None
    startTs: int
    endTs: int
    entryPicId: str
    titlePics: list[str]
    modeTarget: str
    modeDesc: str
    modeRecordDesc: str | None
    extraTag: bool
    modeAvatarPicId: str
    modeAvatarName: str
    modeAvatarText: str
    hasUnlockToast: bool

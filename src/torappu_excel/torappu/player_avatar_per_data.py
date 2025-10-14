from pydantic import BaseModel, ConfigDict

from .player_avatar_group_type import PlayerAvatarGroupType


class PlayerAvatarPerData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    avatarId: str
    avatarType: PlayerAvatarGroupType
    avatarIdSort: int
    avatarIdDesc: str
    avatarItemName: str
    avatarItemDesc: str
    avatarItemUsage: str
    obtainApproach: str
    dynAvatarId: str | None = None

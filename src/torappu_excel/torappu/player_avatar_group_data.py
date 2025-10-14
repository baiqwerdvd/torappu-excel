from pydantic import BaseModel, ConfigDict

from .player_avatar_group_type import PlayerAvatarGroupType


class PlayerAvatarGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    avatarType: PlayerAvatarGroupType
    typeName: str
    sortId: int | None = None
    avatarIdList: list[str]

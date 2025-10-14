from pydantic import BaseModel, ConfigDict

from .player_avatar_group_data import PlayerAvatarGroupData
from .player_avatar_group_type import PlayerAvatarGroupType
from .player_avatar_per_data import PlayerAvatarPerData


class PlayerAvatarData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    defaultAvatarId: str
    avatarList: list[PlayerAvatarPerData]
    avatarTypeData: dict[PlayerAvatarGroupType, PlayerAvatarGroupData]

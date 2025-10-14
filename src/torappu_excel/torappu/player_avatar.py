from pydantic import BaseModel, ConfigDict

from .player_avatar_block import PlayerAvatarBlock


class PlayerAvatar(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    avatar_icon: dict[str, PlayerAvatarBlock]

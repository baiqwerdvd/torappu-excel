from pydantic import BaseModel, ConfigDict

from .player_avatar_type import PlayerAvatarType


class AvatarInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: PlayerAvatarType
    id: str

from pydantic import BaseModel, ConfigDict

from .player_invite_info import PlayerInviteInfo


class PlayerInviteData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    closeAccept: bool
    newInvite: bool
    inviteList: list[PlayerInviteInfo]

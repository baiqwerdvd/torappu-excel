from .player_sandbox_v2 import PlayerSandboxV2
from ..common import BaseStruct


class PlayerSandboxPerm(BaseStruct):
    template: "PlayerSandboxPerm.PlayerSandboxTemplateData"
    isClose: bool

    class PlayerSandboxTemplateData(BaseStruct):
        SANDBOX_V2: dict[str, PlayerSandboxV2]

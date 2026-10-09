from msgspec import field

from .player_sandbox_v2 import PlayerSandboxV2
from .player_sandbox_v2_summary import PlayerSandboxV2Summary
from .player_sandbox_v3 import PlayerSandboxV3
from .player_sandbox_v3_summary import PlayerSandboxV3Summary
from ..common import BaseStruct


class PlayerSandboxPerm(BaseStruct):
    template: "PlayerSandboxPerm.PlayerSandboxTemplateData"
    isClose: bool
    loadTs: int | None = field(default=None)
    pin: str | None = field(default=None)
    summary: "PlayerSandboxPerm.PlayerSandboxSummaryData | None" = field(default=None)
    topic: str | None = field(default=None)

    class PlayerSandboxTemplateData(BaseStruct):
        SANDBOX_V2: dict[str, PlayerSandboxV2 | None]
        SANDBOX_V3: dict[str, PlayerSandboxV3] | None = field(default=None)

    class PlayerSandboxSummaryData(BaseStruct):
        SANDBOX_V2: dict[str, PlayerSandboxV2Summary]
        SANDBOX_V3: dict[str, PlayerSandboxV3Summary]

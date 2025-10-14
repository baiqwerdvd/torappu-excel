from pydantic import BaseModel, ConfigDict

from .player_sandbox_v2 import PlayerSandboxV2


class PlayerSandboxPerm(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    template: "PlayerSandboxPerm.PlayerSandboxTemplateData"
    isClose: bool

    class PlayerSandboxTemplateData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        SANDBOX_V2: dict[str, PlayerSandboxV2]

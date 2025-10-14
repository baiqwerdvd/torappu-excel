from pydantic import BaseModel, ConfigDict

from .player_retro_block import PlayerRetroBlock


class PlayerRetro(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    coin: int
    supplement: bool
    block: dict[str, PlayerRetroBlock]
    lst: int
    nst: int
    trail: dict[str, dict[str, bool]]
    rewardPerm: list[str]

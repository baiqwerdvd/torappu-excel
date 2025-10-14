from enum import IntEnum

from pydantic import BaseModel, ConfigDict

from .player_crisis_social_info import PlayerCrisisSocialInfo


class PlayerCrisisV2Season(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    coin: int | None = None
    permanent: "PlayerCrisisV2Season.PermanentMapInfo"
    temporary: dict[str, "PlayerCrisisV2Season.BasicMapInfo"]
    social: PlayerCrisisSocialInfo

    class RuneState(IntEnum):
        UNKNOWN = 0
        LOCKED = 1
        UNLOCK = 2
        FINISH = 3

    class NodeState(IntEnum):
        INACTIVE = 0
        ACTIVED = 1
        CLAIMED = 2

    class BagState(IntEnum):
        INCOMPLETE = 0
        COMPLETED = 1
        CLAIMED = 2

    class RewardInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        state: "PlayerCrisisV2Season.NodeState"
        progress: int

    class PermanentMapInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        scoreSingle: list[int]
        comment: list[str]
        exRunes: dict[str, "PlayerCrisisV2Season.RuneState"]
        runePack: dict[str, "PlayerCrisisV2Season.BagState"]
        reward: dict[str, "PlayerCrisisV2Season.RewardInfo"]
        state: bool
        scoreTotal: list[int]
        rune: dict[str, "PlayerCrisisV2Season.RuneState"]
        challenge: dict[str, "PlayerCrisisV2Season.NodeState"]

    class BasicMapInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        state: bool
        scoreTotal: list[int]
        rune: dict[str, "PlayerCrisisV2Season.RuneState"]
        challenge: dict[str, "PlayerCrisisV2Season.NodeState"]

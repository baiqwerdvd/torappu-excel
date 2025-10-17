from enum import IntEnum

from .player_crisis_social_info import PlayerCrisisSocialInfo
from ..common import BaseStruct


class PlayerCrisisV2Season(BaseStruct):
    permanent: "PlayerCrisisV2Season.PermanentMapInfo"
    temporary: dict[str, "PlayerCrisisV2Season.BasicMapInfo"]
    social: PlayerCrisisSocialInfo
    coin: int | None = None

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

    class RewardInfo(BaseStruct):
        state: "PlayerCrisisV2Season.NodeState"
        progress: int

    class PermanentMapInfo(BaseStruct):
        scoreSingle: list[int]
        comment: list[str]
        exRunes: dict[str, "PlayerCrisisV2Season.RuneState"]
        runePack: dict[str, "PlayerCrisisV2Season.BagState"]
        reward: dict[str, "PlayerCrisisV2Season.RewardInfo"]
        state: int
        scoreTotal: list[int]
        rune: dict[str, "PlayerCrisisV2Season.RuneState"]
        challenge: dict[str, "PlayerCrisisV2Season.NodeState"]

    class BasicMapInfo(BaseStruct):
        state: int
        scoreTotal: list[int]
        rune: dict[str, "PlayerCrisisV2Season.RuneState"]
        challenge: dict[str, "PlayerCrisisV2Season.NodeState"]

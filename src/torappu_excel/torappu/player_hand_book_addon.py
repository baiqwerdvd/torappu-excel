from msgspec import field

from ..common import BaseStruct


class PlayerHandBookAddon(BaseStruct):
    story: dict[str, "PlayerHandBookAddon.GetInfo"]
    stage: dict[str, "PlayerHandBookAddon.StageInfo"] = field(default_factory=dict)

    class GetInfo(BaseStruct):
        fts: int
        rts: int

    class StageInfo(GetInfo):
        startTimes: int
        completeTimes: int
        state: int
        startTime: int | None = None

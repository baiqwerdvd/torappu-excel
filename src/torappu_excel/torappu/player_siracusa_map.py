from enum import IntEnum

from ..common import BaseStruct


class PlayerSiracusaMap(BaseStruct):
    select: str | None
    card: dict[str, "PlayerSiracusaMap.CharCard"]
    opera: "PlayerSiracusaMap.Opera"
    area: dict[str, int]

    class CharCardItemEnum(IntEnum):
        NONE = 0
        UNUSED = 1
        USED = 2

    class StateEnum(IntEnum):
        NONE = 0
        DOING = 1
        COMPLETED = 2

    class CharCardStatus(IntEnum):
        NONE = 0
        NEW = 1
        DOING = 2
        COMPLETED = 3

    class TaskRingStatus(IntEnum):
        NONE = 0
        DOING = 1
        TAKE_REWARD = 2
        COMPLETED = 3

    class OperaState(IntEnum):
        UNRELEASED = 0
        RELEASE = 1
        RELEASED = 2

    class BattleProgress(BaseStruct):
        value: int
        target: int

    class TaskInfo(BaseStruct):
        state: "PlayerSiracusaMap.StateEnum"
        option: list[str] | None = None
        progress: "PlayerSiracusaMap.BattleProgress | None" = None

    class TaskRing(BaseStruct):
        task: dict[str, "PlayerSiracusaMap.TaskInfo"]
        state: "PlayerSiracusaMap.TaskRingStatus"

    class CharCard(BaseStruct):
        item: dict[str, "PlayerSiracusaMap.CharCardItemEnum"]
        taskRing: dict[str, "PlayerSiracusaMap.TaskRing"]
        state: "PlayerSiracusaMap.CharCardStatus"

    class Opera(BaseStruct):
        total: int
        show: str | None
        release: dict[str, "PlayerSiracusaMap.OperaState"]
        like: dict[str, str]

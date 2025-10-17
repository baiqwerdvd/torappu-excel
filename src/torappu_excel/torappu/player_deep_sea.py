from enum import IntEnum

from ..common import BaseStruct


class PlayerDeepSea(BaseStruct):
    places: dict[str, "PlayerDeepSea.PlaceStatus"]
    nodes: dict[str, "PlayerDeepSea.NodeStatus"]
    choices: dict[str, "list[PlayerDeepSea.ChoiceStatus]"]
    events: dict[str, "PlayerDeepSea.ReadStatus"]
    treasures: dict[str, "PlayerDeepSea.TreasureStatus"]
    stories: dict[str, "PlayerDeepSea.ReadStatus"]
    techTrees: dict[str, "PlayerDeepSea.TechData"]
    logs: dict[str, list[str]]

    class PlaceStatus(IntEnum):
        INVISIBLE = 0
        UNKNOWN = 1
        DISCOVERED = 2

    class NodeStatus(IntEnum):
        LOCKED = 0
        UNLOCK = 1
        TRIGGERED = 2

    class ChoiceStatus(IntEnum):
        LOCKED = 0
        UNLOCK = 1
        SELECTED = 2

    class ReadStatus(IntEnum):
        UNREAD = 0
        READ = 1

    class TreasureStatus(IntEnum):
        NOTGOT = 0
        GOT = 1

    class TechStatus(IntEnum):
        LOCKED = 0
        UNLOCK = 1
        ACTIVED = 2

    class TechData(BaseStruct):
        state: "PlayerDeepSea.TechStatus"
        branch: str

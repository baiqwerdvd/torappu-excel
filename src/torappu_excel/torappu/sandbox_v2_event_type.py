from enum import StrEnum


class SandboxV2EventType(StrEnum):
    NONE = "NONE"
    EVENT = "EVENT"
    MISSION = "MISSION"
    QUEST_EVENT = "QUEST_EVENT"
    QUEST_MISSION = "QUEST_MISSION"

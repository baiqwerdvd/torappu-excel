from enum import StrEnum


class SandboxNodeType(StrEnum):
    NONE = "NONE"
    HOME = "HOME"
    BATTLE = "BATTLE"
    NEST = "NEST"
    COLLECT = "COLLECT"
    HUNT = "HUNT"
    CAVE = "CAVE"
    EVENT = "EVENT"
    MISSION = "MISSION"
    MARKET = "MARKET"

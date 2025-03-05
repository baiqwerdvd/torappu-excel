from ..common import BaseStruct


class RL02DevelopmentLine(BaseStruct):
    fromNode: str
    toNode: str
    fromNodeP: int
    fromNodeR: int
    toNodeP: int
    toNodeR: int
    enrollId: str | None

from ..common import BaseStruct


class SandboxItemTrapData(BaseStruct):
    itemId: str
    trapId: str
    trapPhase: int
    trapLevel: int
    skillIndex: int
    skillLevel: int

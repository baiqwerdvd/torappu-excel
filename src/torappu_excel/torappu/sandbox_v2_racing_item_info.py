from .blackboard import Blackboard
from ..common import BaseStruct


class SandboxV2RacingItemInfo(BaseStruct):
    racerItemId: str
    name: str
    iconId: str
    blackboard: list[Blackboard]

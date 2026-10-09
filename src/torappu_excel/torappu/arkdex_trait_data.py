from .blackboard import Blackboard
from ..common import BaseStruct


class ArkdexTraitData(BaseStruct):
    sortId: int
    traitMask: int
    traitId: str
    name: str
    icon: str
    description: str
    color: str
    buff: list[Blackboard]

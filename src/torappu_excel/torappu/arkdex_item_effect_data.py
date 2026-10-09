from .blackboard import Blackboard
from ..common import BaseStruct


class ArkdexItemEffectData(BaseStruct):
    itemNumId: int
    buff: str
    activeDesc: str
    blackboard: list[Blackboard]

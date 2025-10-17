from .blackboard import Blackboard
from ..common import BaseStruct


class RoguelikeBuff(BaseStruct):
    key: str
    blackboard: list[Blackboard]

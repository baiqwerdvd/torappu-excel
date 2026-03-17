from ..common import BaseStruct


class Act7FunCharAnimData(BaseStruct):
    charId: str
    failAnimId: str
    normalAnimIds: list[str]

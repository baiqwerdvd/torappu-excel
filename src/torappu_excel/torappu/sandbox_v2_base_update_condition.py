from ..common import BaseStruct


class SandboxV2BaseUpdateCondition(BaseStruct):
    desc: str
    limitCond: str
    param: list[str]

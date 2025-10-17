from ..common import BaseStruct


class ConditionalDropInfo(BaseStruct):
    template: str
    param: list[str]
    countLimit: int

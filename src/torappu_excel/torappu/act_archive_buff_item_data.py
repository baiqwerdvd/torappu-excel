from ..common import BaseStruct


class ActArchiveBuffItemData(BaseStruct):
    buffId: str
    buffGroupIndex: int
    innerSortId: int
    name: str
    iconId: str
    usage: str
    desc: str
    color: str

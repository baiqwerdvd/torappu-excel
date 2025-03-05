from ..common import BaseStruct


class RL03DevRawTextBuffGroup(BaseStruct):
    nodeIdList: list[str]
    useLevelMark: bool
    groupIconId: str
    sortId: int

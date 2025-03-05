from ..common import BaseStruct


class RL02DevRawTextBuffGroup(BaseStruct):
    nodeIdList: list[str]
    useLevelMark: bool
    groupIconId: str
    useUpBreak: bool
    sortId: int

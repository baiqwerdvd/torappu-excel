from ..common import BaseStruct


class StageDiffGroupTable(BaseStruct):
    normalId: str
    toughId: str | None
    easyId: str

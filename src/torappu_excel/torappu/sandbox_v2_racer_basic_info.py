from ..common import BaseStruct


class SandboxV2RacerBasicInfo(BaseStruct):
    racerId: str
    sortId: int
    racerName: str
    itemId: str
    attributeMaxValue: list[int]

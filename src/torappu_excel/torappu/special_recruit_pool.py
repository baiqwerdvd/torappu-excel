from .item_bundle import ItemBundle
from ..common import BaseStruct


class SpecialRecruitPool(BaseStruct):
    endDateTime: int
    order: int
    recruitId: str
    recruitTimeTable: list["SpecialRecruitPool.SpecialRecruitCostData"]
    startDateTime: int
    tagId: int
    tagName: str
    CDPrimColor: str | None
    CDSecColor: str | None
    LMTGSID: str | None
    gachaRuleType: str

    class SpecialRecruitCostData(BaseStruct):
        itemCosts: ItemBundle
        recruitPrice: int
        timeLength: int

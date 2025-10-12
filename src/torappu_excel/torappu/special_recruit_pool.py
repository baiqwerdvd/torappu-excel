from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class SpecialRecruitPool(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class SpecialRecruitCostData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemCosts: ItemBundle
        recruitPrice: int
        timeLength: int

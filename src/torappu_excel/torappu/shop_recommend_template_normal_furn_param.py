from ..common import BaseStruct


class ShopRecommendTemplateNormalFurnParam(BaseStruct):
    showStartTs: int
    showEndTs: int
    furnPackId: str
    isNew: bool
    isPackSell: bool
    count: int
    colorBack: str
    colorText: str
    actId: str | None

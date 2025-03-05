from ..common import BaseStruct


class ShopRecommendTemplateNormalGiftParam(BaseStruct):
    showStartTs: int
    showEndTs: int
    goodId: str
    giftPackageName: str
    price: int
    logoId: str
    color: str
    haveMark: bool
    availCount: int = 0

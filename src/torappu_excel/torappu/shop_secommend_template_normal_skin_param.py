from ..common import BaseStruct


class ShopRecommendTemplateNormalSkinParam(BaseStruct):
    showStartTs: int
    showEndTs: int
    skinIds: list[str]
    skinGroupName: str
    brandIconId: str
    colorBack: str
    colorText: str
    text: str

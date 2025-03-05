from .shop_recommend_template_normal_furn_param import ShopRecommendTemplateNormalFurnParam
from .shop_recommend_template_normal_gift_param import ShopRecommendTemplateNormalGiftParam
from .shop_recommend_template_return_skin_param import ShopRecommendTemplateReturnSkinParam
from .shop_secommend_template_normal_skin_param import ShopRecommendTemplateNormalSkinParam
from ..common import BaseStruct

from msgspec import field


class ShopRecommendTemplateParam(BaseStruct):
    normalGiftParam: ShopRecommendTemplateNormalGiftParam | None = field(default=None)
    normalSkinParam: ShopRecommendTemplateNormalSkinParam | None = field(default=None)
    normalFurnParam: ShopRecommendTemplateNormalFurnParam | None = field(default=None)
    returnSkinParam: ShopRecommendTemplateReturnSkinParam | None = field(default=None)

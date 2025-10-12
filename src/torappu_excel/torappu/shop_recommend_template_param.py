from pydantic import BaseModel, ConfigDict, Field

from .shop_recommend_template_normal_furn_param import ShopRecommendTemplateNormalFurnParam
from .shop_recommend_template_normal_gift_param import ShopRecommendTemplateNormalGiftParam
from .shop_recommend_template_return_skin_param import ShopRecommendTemplateReturnSkinParam
from .shop_secommend_template_normal_skin_param import ShopRecommendTemplateNormalSkinParam


class ShopRecommendTemplateParam(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    normalGiftParam: ShopRecommendTemplateNormalGiftParam | None = Field(default=None)
    normalSkinParam: ShopRecommendTemplateNormalSkinParam | None = Field(default=None)
    normalFurnParam: ShopRecommendTemplateNormalFurnParam | None = Field(default=None)
    returnSkinParam: ShopRecommendTemplateReturnSkinParam | None = Field(default=None)

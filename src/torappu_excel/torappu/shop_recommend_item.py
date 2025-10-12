from pydantic import BaseModel, ConfigDict

from .recommend_item_tag_tips import RecommendItemTagTips
from .shop_keeper_word import ShopKeeperWord
from .shop_recommend_group import ShopRecommendGroup
from .shop_recommend_template_param import ShopRecommendTemplateParam
from .shop_recommend_template_type import ShopRecommendTemplateType


class ShopRecommendItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    tagId: str
    displayType: str
    tagName: str
    itemTag: RecommendItemTagTips
    orderNum: int
    startDatetime: int
    endDatetime: int
    groupList: list[ShopRecommendGroup]
    tagWord: ShopKeeperWord
    templateType: ShopRecommendTemplateType
    templateParam: ShopRecommendTemplateParam | None

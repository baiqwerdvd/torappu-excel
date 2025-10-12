from pydantic import BaseModel, ConfigDict

from .shop_recommend_data import ShopRecommendData


class ShopRecommendGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    recommendGroup: list[int]
    dataList: list[ShopRecommendData]

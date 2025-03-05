from .shop_recommend_data import ShopRecommendData
from ..common import BaseStruct


class ShopRecommendGroup(BaseStruct):
    recommendGroup: list[int]
    dataList: list[ShopRecommendData]

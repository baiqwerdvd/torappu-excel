from .default_shop_data import DefaultShopData
from .default_zone_data import DefaultZoneData
from ..common import BaseStruct


class DefaultFirstData(BaseStruct):
    zoneList: list[DefaultZoneData]
    shopList: list[DefaultShopData] | None

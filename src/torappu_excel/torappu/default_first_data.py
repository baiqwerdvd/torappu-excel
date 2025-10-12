from pydantic import BaseModel, ConfigDict

from .default_shop_data import DefaultShopData
from .default_zone_data import DefaultZoneData


class DefaultFirstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneList: list[DefaultZoneData]
    shopList: list[DefaultShopData] | None

from pydantic import BaseModel, ConfigDict, Field

from .furn_shop_display_place import FurnShopDisplayPlace


class FurniShopObject(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goodId: str
    furniId: str
    displayName: str
    shopDisplay: FurnShopDisplayPlace
    priceCoin: int
    priceDia: int
    discount: float | int
    originPriceCoin: int
    originPriceDia: int
    end: int
    count: int
    sequence: int
    begin: int | None = Field(default=None)

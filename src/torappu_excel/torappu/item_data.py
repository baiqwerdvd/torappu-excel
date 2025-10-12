from pydantic import BaseModel, ConfigDict, Field

from .building_data import BuildingData
from .item_classify_type import ItemClassifyType
from .item_drop_shop_type import ItemDropShopType
from .item_rarity import ItemRarity
from .item_type import ItemType
from .occ_per import OccPer


class ItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    name: str
    description: str | None
    rarity: ItemRarity
    iconId: str
    overrideBkg: None
    stackIconId: str | None
    sortId: int
    usage: str | None
    obtainApproach: str | None
    classifyType: ItemClassifyType
    itemType: ItemType
    stageDropList: list["ItemData.StageDropInfo"]
    buildingProductList: list["ItemData.BuildingProductInfo"]
    shopRelateInfoList: list["ItemData.ShopRelateInfo"] | None
    voucherRelateList: list["ItemData.VoucherRelateInfo"] | None = Field(default=None)
    hideInItemGet: bool | None = Field(default=None)

    class StageDropInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        occPer: OccPer
        sortId: int

    class BuildingProductInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        roomType: "BuildingData.RoomType"
        formulaId: str

    class VoucherRelateInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        voucherId: str
        voucherItemType: ItemType

    class ShopRelateInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        shopType: ItemDropShopType
        shopGroup: int
        startTs: int

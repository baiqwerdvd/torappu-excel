from msgspec import field

from .building_data import BuildingData
from .item_classify_type import ItemClassifyType
from .item_drop_shop_type import ItemDropShopType
from .item_rarity import ItemRarity
from .item_type import ItemType
from .occ_per import OccPer
from ..common import BaseStruct


class ItemData(BaseStruct):
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
    voucherRelateList: list["ItemData.VoucherRelateInfo"] | None = field(default=None)
    hideInItemGet: bool | None = field(default=None)

    class StageDropInfo(BaseStruct):
        stageId: str
        occPer: OccPer
        sortId: int

    class BuildingProductInfo(BaseStruct):
        roomType: "BuildingData.RoomType"
        formulaId: str

    class VoucherRelateInfo(BaseStruct):
        voucherId: str
        voucherItemType: ItemType

    class ShopRelateInfo(BaseStruct):
        shopType: ItemDropShopType
        shopGroup: int
        startTs: int

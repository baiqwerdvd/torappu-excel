from .building_data import BuildingData
from .item_classify_type import ItemClassifyType
from .item_rarity import ItemRarity
from .item_type import ItemType
from .occ_per import OccPer
from ..common import BaseStruct

from msgspec import field


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
    voucherRelateList: list["ItemData.VoucherRelateInfo"] | None = field(default=None)
    hideInItemGet: bool | None = field(default=None)

    class StageDropInfo(BaseStruct):
        stageId: str
        occPer: OccPer

    class BuildingProductInfo(BaseStruct):
        roomType: "BuildingData.RoomType"
        formulaId: str

    class VoucherRelateInfo(BaseStruct):
        voucherId: str
        voucherItemType: ItemType

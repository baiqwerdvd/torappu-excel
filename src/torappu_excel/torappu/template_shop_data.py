from .item_bundle import ItemBundle
from .item_type import ItemType
from .tshop_type import TShopType
from ..common import BaseStruct, CustomIntEnum


class TemplateShopData(BaseStruct):
    shopId: str
    shopName: str
    type: TShopType
    price: ItemBundle
    shopGroup: dict[str, "TemplateShopData.TShopGroup"]
    iconColorCodes: str
    buttonColorCodes: str
    startTime: int
    endTime: int
    groupExtraData: "TemplateShopData.GroupShopExtraData | None"
    accumulativePrizeGoods: dict[str, "TemplateShopData.ShopAccumulativePrizeItem"]

    class GoodType(CustomIntEnum):
        NORMAL = "NORMAL", 0
        PROGRESS = "PROGRESS", 1

    class GroupShopExtraData(BaseStruct):
        inTimeText: str
        allEndText: str

    class ProgessGoodItem(BaseStruct):
        order: int
        price: int
        displayName: str
        item: ItemBundle

    class ShopAccumulativePrizeItem(BaseStruct):
        prizeId: str
        sortId: int
        picId: str
        itemId: str
        itemType: ItemType
        count: int
        costTotal: int
        acquireTitle: str
        displayName: str
        displayDiscription: str

    class ShopGood(BaseStruct):
        goodId: str
        displayName: str | None
        sortId: int
        goodType: "TemplateShopData.GoodType"
        item: ItemBundle
        progressGoodId: str | None
        price: int
        availCount: int

    class TShopGroup(BaseStruct):
        shopGroupId: str
        sortId: int
        preGroup: str | None
        bkgIconId: str | None
        lockDesc: str | None
        shopGood: dict[str, "TemplateShopData.ShopGood"]
        progressGoods: dict[str, "list[TemplateShopData.ProgessGoodItem]"]

from .choose_shop_relation import ChooseShopRelation
from .lmtgs_shop_overlay_schedule import LMTGSShopOverlaySchedule
from .lmtgs_shop_schedule import LMTGSShopSchedule
from .shop_carousel_data import ShopCarouselData
from .shop_client_gp_data import ShopClientGPData
from .shop_credit_unlock_group import ShopCreditUnlockGroup
from .shop_gp_tab_display_data import ShopGPTabDisplayData
from .shop_keeper_word import ShopKeeperWord
from .shop_recommend_item import ShopRecommendItem
from .shop_unlock_type import ShopUnlockType
from ..common import BaseStruct


class ShopClientData(BaseStruct):
    recommendList: list[ShopRecommendItem]
    creditUnlockGroup: dict[str, ShopCreditUnlockGroup]
    shopKeeperData: "ShopClientData.ShopKeeperData"
    carousels: list[ShopCarouselData]
    chooseShopRelations: list[ChooseShopRelation]
    shopUnlockDict: dict[str, ShopUnlockType]
    extraQCShopRule: list[str]
    repQCShopRule: list[str]
    shopGPDataDict: dict[str, ShopClientGPData]
    tabDisplayData: dict[str, ShopGPTabDisplayData]
    shopMonthlySubGoodId: str
    ls: list[LMTGSShopSchedule]
    os: list[LMTGSShopOverlaySchedule]

    class ShopKeeperData(BaseStruct):
        welcomeWords: list[ShopKeeperWord]
        clickWords: list[ShopKeeperWord]

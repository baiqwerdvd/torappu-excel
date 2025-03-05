from enum import StrEnum

from .common_favor_up_info import CommonFavorUpInfo
from .item_bundle import ItemBundle
from ..common import BaseStruct

from msgspec import field


class Act3D0Data(BaseStruct):
    class GoodType(StrEnum):
        NORMAL = "NORMAL"
        SPECIAL = "SPECIAL"

    class GachaBoxType(StrEnum):
        LIMITED = "LIMITED"
        UNLIMITED = "UNLIMITED"

    campBasicInfo: dict[str, "Act3D0Data.CampBasicInfo"]
    limitedPoolList: dict[str, "Act3D0Data.LimitedPoolDetailInfo"]
    infinitePoolList: dict[str, "Act3D0Data.InfinitePoolDetailInfo"]
    infinitePercent: dict[str, "Act3D0Data.InfinitePoolPercent"] | None
    campItemMapInfo: dict[str, "Act3D0Data.CampItemMapInfo"]
    clueInfo: dict[str, "Act3D0Data.ClueInfo"]
    mileStoneInfo: list["Act3D0Data.MileStoneInfo"]
    mileStoneTokenId: str
    coinTokenId: str
    etTokenId: str
    gachaBoxInfo: list["Act3D0Data.GachaBoxInfo"]
    campInfo: dict[str, "Act3D0Data.CampInfo"] | None
    zoneDesc: dict[str, "Act3D0Data.ZoneDescInfo"]
    favorUpList: dict[str, CommonFavorUpInfo] | None

    class CampBasicInfo(BaseStruct):
        campId: str
        campName: str
        campDesc: str
        rewardDesc: str | None

    class LimitedPoolDetailInfo(BaseStruct):
        poolId: str
        poolItemInfo: list["Act3D0Data.LimitedPoolDetailInfo.PoolItemInfo"]

        class PoolItemInfo(BaseStruct):
            goodId: str
            itemInfo: ItemBundle | None
            goodType: "Act3D0Data.GoodType"
            perCount: int
            totalCount: int
            weight: int
            type_: str = field(name="type")
            orderId: int

    class InfinitePoolDetailInfo(BaseStruct):
        poolId: str
        poolItemInfo: list["Act3D0Data.InfinitePoolDetailInfo.PoolItemInfo"]

        class PoolItemInfo(BaseStruct):
            goodId: str
            itemInfo: ItemBundle
            goodType: "Act3D0Data.GoodType"
            perCount: int
            weight: int
            type_: str = field(name="type")
            orderId: int

    class InfinitePoolPercent(BaseStruct):
        percentDict: dict[str, int]

    class CampItemMapInfo(BaseStruct):
        goodId: str
        itemDict: dict[str, ItemBundle]

    class ClueInfo(BaseStruct):
        itemId: str
        campId: str
        orderId: int
        imageId: str

    class MileStoneInfo(BaseStruct):
        mileStoneId: str
        orderId: int
        mileStoneType: "Act3D0Data.GoodType"
        normalItem: ItemBundle | None
        specialItemDict: dict[str, ItemBundle]
        tokenNum: int

    class GachaBoxInfo(BaseStruct):
        gachaBoxId: str
        boxType: "Act3D0Data.GachaBoxType"
        keyGoodId: str | None
        tokenId: ItemBundle
        tokenNumOnce: int
        unlockImg: str | None
        nextGachaBoxInfoId: str | None

    class CampInfo(BaseStruct):
        campId: str
        campChineseName: str

    class ZoneDescInfo(BaseStruct):
        zoneId: str
        lockedText: str | None

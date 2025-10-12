from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .common_favor_up_info import CommonFavorUpInfo
from .item_bundle import ItemBundle


class Act3D0Data(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class CampBasicInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        campId: str
        campName: str
        campDesc: str
        rewardDesc: str | None

    class LimitedPoolDetailInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        poolId: str
        poolItemInfo: list["Act3D0Data.LimitedPoolDetailInfo.PoolItemInfo"]

        class PoolItemInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            goodId: str
            itemInfo: ItemBundle | None
            goodType: "Act3D0Data.GoodType"
            perCount: int
            totalCount: int
            weight: int
            type: str
            orderId: int

    class InfinitePoolDetailInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        poolId: str
        poolItemInfo: list["Act3D0Data.InfinitePoolDetailInfo.PoolItemInfo"]

        class PoolItemInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            goodId: str
            itemInfo: ItemBundle
            goodType: "Act3D0Data.GoodType"
            perCount: int
            weight: int
            type: str
            orderId: int

    class InfinitePoolPercent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        percentDict: dict[str, int]

    class CampItemMapInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        goodId: str
        itemDict: dict[str, ItemBundle]

    class ClueInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemId: str
        campId: str
        orderId: int
        imageId: str

    class MileStoneInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        mileStoneId: str
        orderId: int
        mileStoneType: "Act3D0Data.GoodType"
        normalItem: ItemBundle | None
        specialItemDict: dict[str, ItemBundle]
        tokenNum: int

    class GachaBoxInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        gachaBoxId: str
        boxType: "Act3D0Data.GachaBoxType"
        keyGoodId: str | None
        tokenId: ItemBundle
        tokenNumOnce: int
        unlockImg: str | None
        nextGachaBoxInfoId: str | None

    class CampInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        campId: str
        campChineseName: str

    class ZoneDescInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        lockedText: str | None

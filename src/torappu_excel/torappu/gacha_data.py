# pyright: reportMissingTypeArgument=false
from .gacha_pool_client_data import GachaPoolClientData
from .gacha_tag import GachaTag
from .newbee_gacha_pool_client_data import NewbeeGachaPoolClientData
from .potential_material_converter_config import PotentialMaterialConverterConfig
from .recruit_pool import RecruitPool
from .special_recruit_pool import SpecialRecruitPool
from ..common import BaseStruct

from msgspec import field


class GachaData(BaseStruct):
    gachaPoolClient: list[GachaPoolClientData]
    newbeeGachaPoolClient: list[NewbeeGachaPoolClientData]
    specialRecruitPool: list[SpecialRecruitPool]
    gachaTags: list[GachaTag]
    recruitPool: RecruitPool
    potentialMaterialConverter: PotentialMaterialConverterConfig
    classicPotentialMaterialConverter: PotentialMaterialConverterConfig
    recruitRarityTable: dict[str, "GachaData.RecruitRange"]
    specialTagRarityTable: dict[str, list[int]]
    recruitDetail: str
    showGachaLogEntry: bool
    carousel: list["GachaData.CarouselData"]
    freeGacha: list["GachaData.FreeLimitGachaData"]
    limitTenGachaItem: list["GachaData.LimitTenGachaTkt"]
    linkageTenGachaItem: list["GachaData.LinkageTenGachaTkt"]
    normalGachaItem: list["GachaData.NormalGachaTkt"]
    fesGachaPoolRelateItem: dict[str, "GachaData.FesGachaPoolRelateItem"] | None
    dicRecruit6StarHint: dict[str, str] | None
    specialGachaPercentDict: dict[str, float]
    gachaTagMaxValid: int | None = field(default=None)
    potentialMats: dict | None = field(default=None)
    classicPotentialMats: dict | None = field(default=None)

    class RecruitRange(BaseStruct):
        rarityStart: int
        rarityEnd: int

    class CarouselData(BaseStruct):
        poolId: str
        index: int
        startTime: int
        endTime: int
        spriteId: str

    class FreeLimitGachaData(BaseStruct):
        poolId: str
        openTime: int
        endTime: int
        freeCount: int

    class LimitTenGachaTkt(BaseStruct):
        itemId: str
        endTime: int

    class LinkageTenGachaTkt(BaseStruct):
        itemId: str
        endTime: int
        gachaPoolId: str

    class NormalGachaTkt(BaseStruct):
        itemId: str
        endTime: int
        gachaPoolId: str
        isTen: bool

    class FesGachaPoolRelateItem(BaseStruct):
        rarityRank5ItemId: str
        rarityRank6ItemId: str

# pyright: reportMissingTypeArgument=false
from pydantic import BaseModel, ConfigDict, Field

from .gacha_pool_client_data import GachaPoolClientData
from .gacha_tag import GachaTag
from .newbee_gacha_pool_client_data import NewbeeGachaPoolClientData
from .potential_material_converter_config import PotentialMaterialConverterConfig
from .recruit_pool import RecruitPool
from .special_recruit_pool import SpecialRecruitPool


class GachaData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
    gachaTagMaxValid: int | None = Field(default=None)
    potentialMats: dict | None = Field(default=None)
    classicPotentialMats: dict | None = Field(default=None)

    class RecruitRange(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        rarityStart: int
        rarityEnd: int

    class CarouselData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        poolId: str
        index: int
        startTime: int
        endTime: int
        spriteId: str

    class FreeLimitGachaData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        poolId: str
        openTime: int
        endTime: int
        freeCount: int

    class LimitTenGachaTkt(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemId: str
        endTime: int

    class LinkageTenGachaTkt(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemId: str
        endTime: int
        gachaPoolId: str

    class NormalGachaTkt(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemId: str
        endTime: int
        gachaPoolId: str
        isTen: bool

    class FesGachaPoolRelateItem(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        rarityRank5ItemId: str
        rarityRank6ItemId: str

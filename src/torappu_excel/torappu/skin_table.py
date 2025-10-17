from .char_skin_brand_info import CharSkinBrandInfo
from .char_skin_data import CharSkinData
from .sp_dyn_illust_info import SpDynIllustInfo
from .special_skin_info import SpecialSkinInfo
from ..common import BaseStruct


class SkinTable(BaseStruct):
    charSkins: dict[str, CharSkinData]
    buildinEvolveMap: dict[str, dict[str, str]]
    buildinPatchMap: dict[str, dict[str, str]]
    brandList: dict[str, CharSkinBrandInfo]
    specialSkinInfoList: list[SpecialSkinInfo]
    spDynSkins: dict[str, SpDynIllustInfo]
    spDynIllustSkinTagsMap: dict[str, str]

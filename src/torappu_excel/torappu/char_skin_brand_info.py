from .char_skin_group_info import CharSkinGroupInfo
from .char_skin_kv_img_info import CharSkinKvImgInfo
from ..common import BaseStruct


class CharSkinBrandInfo(BaseStruct):
    brandId: str
    groupList: list[CharSkinGroupInfo]
    kvImgIdList: list[CharSkinKvImgInfo]
    brandName: str
    brandCapitalName: str
    description: str
    publishTime: int
    sortId: int

from pydantic import BaseModel, ConfigDict

from .char_skin_group_info import CharSkinGroupInfo
from .char_skin_kv_img_info import CharSkinKvImgInfo


class CharSkinBrandInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    brandId: str
    groupList: list[CharSkinGroupInfo]
    kvImgIdList: list[CharSkinKvImgInfo]
    brandName: str
    brandCapitalName: str
    description: str
    publishTime: int
    sortId: int

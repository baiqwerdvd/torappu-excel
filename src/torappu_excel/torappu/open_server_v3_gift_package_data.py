from ..common import BaseStruct


class OpenServerV3GiftPackageData(BaseStruct):
    giftPackageId: str
    goodId: str
    giftPackagePic: str
    sortId: int
    isLimit: bool

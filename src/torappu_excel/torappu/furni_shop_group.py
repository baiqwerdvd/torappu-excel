from ..common import BaseStruct


class FurniShopGroup(BaseStruct):
    packageId: str
    icon: str
    name: str
    description: str
    sequence: int
    saleBegin: int
    saleEnd: int
    decoration: int
    goodList: list["FurniShopGroup.GoodData"]
    eventGoodList: list["FurniShopGroup.EventGoodData"]
    imageList: list["FurniShopGroup.ImageDisplayData"]

    class GoodData(BaseStruct):
        goodId: str
        count: int
        set: str
        sequence: int

    class EventGoodData(BaseStruct):
        name: str
        count: int
        furniId: str
        set: str
        sequence: int

    class ImageDisplayData(BaseStruct):
        picId: str
        index: int

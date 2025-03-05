from ..common import BaseStruct

from msgspec import field


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
        set_: str = field(name="set")
        sequence: int

    class EventGoodData(BaseStruct):
        name: str
        count: int
        furniId: str
        set_: str = field(name="set")
        sequence: int

    class ImageDisplayData(BaseStruct):
        picId: str
        index: int

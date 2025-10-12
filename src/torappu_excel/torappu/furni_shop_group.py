from pydantic import BaseModel, ConfigDict


class FurniShopGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class GoodData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        goodId: str
        count: int
        set: str
        sequence: int

    class EventGoodData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        name: str
        count: int
        furniId: str
        set: str
        sequence: int

    class ImageDisplayData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        picId: str
        index: int

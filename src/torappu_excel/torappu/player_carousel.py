from pydantic import BaseModel, ConfigDict


class PlayerCarousel(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    furnitureShop: "PlayerCarousel.PlayerCarouselFurnitureShopData"

    class PlayerCarouselFurnitureShopData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        goods: dict[str, int]
        groups: dict[str, int]

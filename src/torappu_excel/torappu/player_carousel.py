from ..common import BaseStruct


class PlayerCarousel(BaseStruct):
    furnitureShop: "PlayerCarousel.PlayerCarouselFurnitureShopData"

    class PlayerCarouselFurnitureShopData(BaseStruct):
        goods: dict[str, int]
        groups: dict[str, int]

from .player_art_magazine_leaf_data import PlayerArtMagazineLeafData
from ..common import BaseStruct


class PlayerGallery(BaseStruct):
    firstRewards: int
    leafMap: dict[str, PlayerArtMagazineLeafData]
    magazineSquad: list[str]
    collectionRewards: dict[str, int]
    stickerMap: dict[str, int]

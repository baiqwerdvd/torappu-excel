from .art_magazine_leaf_element_data import ArtMagazineLeafElementData
from ..common import BaseStruct


class PlayerArtMagazineLeafData(BaseStruct):
    getTs: int
    version: int
    leafId: str
    decorList: list[ArtMagazineLeafElementData]
    charSkin: ArtMagazineLeafElementData | None

from .art_magazine_leaf_element_data import ArtMagazineLeafElementData
from ..common import BaseStruct


class ArtMagazineLeafData(BaseStruct):
    leafId: str
    decorList: list[ArtMagazineLeafElementData]
    charSkin: ArtMagazineLeafElementData

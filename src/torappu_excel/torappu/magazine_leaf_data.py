from .art_magazine_leaf_data import ArtMagazineLeafData
from .magazine_leaf_const import MagazineLeafConst
from .magazine_leaf_decor_type_data import MagazineLeafDecorTypeData
from .magazine_leaf_item_data import MagazineLeafItemData
from .magazine_leaf_type_data import MagazineLeafTypeData
from ..common import BaseStruct


class MagazineLeafData(BaseStruct):
    leafMap: dict[str, MagazineLeafItemData]
    leafDecorTypeMap: dict[str, MagazineLeafDecorTypeData]
    leafTypeMap: dict[str, MagazineLeafTypeData]
    leafTemplateMap: dict[str, ArtMagazineLeafData]
    constData: MagazineLeafConst
    blackListInDiy: dict[str, dict[str, int]]

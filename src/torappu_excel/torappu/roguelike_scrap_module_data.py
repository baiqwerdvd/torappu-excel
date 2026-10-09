from .grid_position import GridPosition
from .roguelike_scrap_goods_data import RoguelikeScrapGoodsData
from .roguelike_scrap_module_consts import RoguelikeScrapModuleConsts
from .roguelike_scrap_move_data import RoguelikeScrapMoveData
from .roguelike_scrap_passive_data import RoguelikeScrapPassiveData
from .roguelike_scrap_type import RoguelikeScrapType
from .roguelike_scrap_type_data import RoguelikeScrapTypeData
from .shared_consts import SharedConsts
from ..common import BaseStruct


class RoguelikeScrapModuleData(BaseStruct):
    scrapItemToType: dict[str, RoguelikeScrapType]
    scrapTypeData: dict[str, RoguelikeScrapTypeData]
    moveScrapData: dict[str, RoguelikeScrapMoveData]
    goodsScrapData: dict[str, RoguelikeScrapGoodsData]
    passiveScrapData: dict[str, RoguelikeScrapPassiveData]
    moveScrapRangeData: dict[str, "RoguelikeScrapModuleData.RangeData"]
    moduleConsts: RoguelikeScrapModuleConsts

    class RangeData(BaseStruct):
        id: str
        direction: SharedConsts.DirectionStr
        grids: list[GridPosition]

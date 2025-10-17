from .roguelike_san_check_consts import RoguelikeSanCheckConsts
from .roguelike_san_range_data import RoguelikeSanRangeData
from ..common import BaseStruct


class RoguelikeSanCheckModuleData(BaseStruct):
    sanRanges: list[RoguelikeSanRangeData]
    moduleConsts: RoguelikeSanCheckConsts

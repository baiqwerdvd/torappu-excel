from .medal_per_data import MedalPerData
from .medal_type_data import MedalTypeData
from ..common import BaseStruct


class MedalData(BaseStruct):
    medalList: list[MedalPerData]
    medalTypeData: dict[str, MedalTypeData]

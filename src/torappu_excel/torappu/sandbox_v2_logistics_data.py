from .profession_category import ProfessionCategory
from ..common import BaseStruct


class SandboxV2LogisticsData(BaseStruct):
    id: str
    desc: str
    noBuffDesc: str
    iconId: str
    profession: ProfessionCategory
    sortId: int
    levelParams: list[str]

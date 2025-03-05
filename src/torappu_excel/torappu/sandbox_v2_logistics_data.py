from .profession_category import ProfessionCategory
from ..common import BaseStruct

from msgspec import field


class SandboxV2LogisticsData(BaseStruct):
    id_: str = field(name="id")
    desc: str
    noBuffDesc: str
    iconId: str
    profession: ProfessionCategory
    sortId: int
    levelParams: list[str]

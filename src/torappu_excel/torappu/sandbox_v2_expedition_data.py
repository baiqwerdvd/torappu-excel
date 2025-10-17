from .profession_category import ProfessionCategory
from .profession_id import ProfessionID
from ..common import BaseStruct


class SandboxV2ExpeditionData(BaseStruct):
    expeditionId: str
    desc: str
    effectDesc: str
    costAction: int
    costDrink: int
    charCnt: int
    profession: ProfessionCategory | int
    professions: list[ProfessionID]
    minEliteRank: int
    duration: int

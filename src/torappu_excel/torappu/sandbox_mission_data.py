from .profession_id import ProfessionID
from ..common import BaseStruct


class SandboxMissionData(BaseStruct):
    missionId: str
    desc: str
    effectDesc: str | None
    costAction: int
    charCnt: int
    professionIds: list[ProfessionID]
    profession: int
    costStamina: int

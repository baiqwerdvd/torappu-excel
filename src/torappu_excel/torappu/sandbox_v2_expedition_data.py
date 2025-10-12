from pydantic import BaseModel, ConfigDict

from .profession_category import ProfessionCategory
from .profession_id import ProfessionID


class SandboxV2ExpeditionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

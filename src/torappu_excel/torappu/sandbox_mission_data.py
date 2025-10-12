from pydantic import BaseModel, ConfigDict

from .profession_id import ProfessionID


class SandboxMissionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    missionId: str
    desc: str
    effectDesc: str | None
    costAction: int
    charCnt: int
    professionIds: list[ProfessionID]
    profession: int
    costStamina: int

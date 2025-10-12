from pydantic import BaseModel, ConfigDict

from .sandbox_v2_racer_talent_type import SandboxV2RacerTalentType


class SandboxV2RacerTalentInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    talentId: str
    talentType: SandboxV2RacerTalentType
    talentIconId: str
    desc: str

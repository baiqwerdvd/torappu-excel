from pydantic import BaseModel, ConfigDict

from .sandbox_v2_racer_name_type import SandboxV2RacerNameType


class SandboxV2RacerNameInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nameId: str
    nameType: SandboxV2RacerNameType
    nameDesc: str

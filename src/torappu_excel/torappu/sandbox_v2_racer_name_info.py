from .sandbox_v2_racer_name_type import SandboxV2RacerNameType
from ..common import BaseStruct


class SandboxV2RacerNameInfo(BaseStruct):
    nameId: str
    nameType: SandboxV2RacerNameType
    nameDesc: str

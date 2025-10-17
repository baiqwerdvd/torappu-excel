from .sandbox_v2_racer_talent_type import SandboxV2RacerTalentType
from ..common import BaseStruct


class SandboxV2RacerTalentInfo(BaseStruct):
    talentId: str
    talentType: SandboxV2RacerTalentType
    talentIconId: str
    desc: str

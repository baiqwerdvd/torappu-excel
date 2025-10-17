from .sandbox_v2_season_type import SandboxV2SeasonType
from ..common import BaseStruct


class SandboxV2SeasonData(BaseStruct):
    seasonType: SandboxV2SeasonType
    name: str
    functionDesc: str
    description: str
    color: str

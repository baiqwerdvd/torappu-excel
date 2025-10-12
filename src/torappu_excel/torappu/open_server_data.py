from pydantic import BaseModel, ConfigDict

from .chain_login_data import ChainLoginData
from .mission_data import MissionData
from .mission_group import MissionGroup
from .total_checkin_data import TotalCheckinData


class OpenServerData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    openServerMissionGroup: MissionGroup
    openServerMissionData: list[MissionData]
    checkInData: list[TotalCheckinData]
    chainLoginData: list[ChainLoginData]
    totalCheckinCharData: list[str]
    chainLoginCharData: list[str]

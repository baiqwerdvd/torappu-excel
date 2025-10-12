from pydantic import BaseModel, ConfigDict

from .return_v2_mission_item_data import ReturnV2MissionItemData


class ReturnV2MissionGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    sortId: int
    tabTitle: str
    title: str
    desc: str
    diffMissionCount: int
    startTime: int
    endTime: int
    imageId: str
    iconId: str
    missionList: list[ReturnV2MissionItemData]

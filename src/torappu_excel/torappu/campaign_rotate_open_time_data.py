from ..common import BaseStruct


class CampaignRotateOpenTimeData(BaseStruct):
    groupId: str
    stageId: str
    mapId: str
    unknownRegions: list[str]
    duration: int
    startTs: int
    endTs: int

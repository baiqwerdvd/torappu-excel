from ..common import BaseStruct


class CampaignTrainingOpenTimeData(BaseStruct):
    groupId: str
    stages: list[str]
    startTs: int
    endTs: int

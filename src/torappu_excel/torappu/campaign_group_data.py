from ..common import BaseStruct


class CampaignGroupData(BaseStruct):
    groupId: str
    activeCamps: list[str]
    startTs: int
    endTs: int

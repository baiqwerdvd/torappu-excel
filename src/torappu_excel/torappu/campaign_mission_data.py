from ..common import BaseStruct


class CampaignMissionData(BaseStruct):
    id: str
    sortId: int
    param: list[str]
    description: str
    breakFeeAdd: int

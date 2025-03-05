from ..common import BaseStruct

from msgspec import field


class CampaignMissionData(BaseStruct):
    id_: str = field(name="id")
    sortId: int
    param: list[str]
    description: str
    breakFeeAdd: int

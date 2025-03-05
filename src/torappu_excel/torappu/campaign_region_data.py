from ..common import BaseStruct

from msgspec import field


class CampaignRegionData(BaseStruct):
    id_: str = field(name="id")
    isUnknwon: int

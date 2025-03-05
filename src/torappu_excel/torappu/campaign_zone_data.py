from ..common import BaseStruct

from msgspec import field


class CampaignZoneData(BaseStruct):
    id_: str = field(name="id")
    name: str
    regionId: str
    templateId: str

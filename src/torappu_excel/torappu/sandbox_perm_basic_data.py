from .sandbox_perm_template_type import SandboxPermTemplateType
from ..common import BaseStruct


class SandboxPermBasicData(BaseStruct):
    topicId: str
    topicTemplate: SandboxPermTemplateType
    topicName: str
    topicStartTime: int
    fullStoredTime: int
    sortId: int
    priceItemId: str
    templateShopId: str
    homeEntryDisplayData: list["SandboxPermBasicData.HomeEntryDisplayData"]
    webBusType: str
    medalGroupId: str

    class HomeEntryDisplayData(BaseStruct):
        displayId: str
        topicId: str
        startTs: int
        endTs: int

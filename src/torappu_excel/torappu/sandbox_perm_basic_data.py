from pydantic import BaseModel, ConfigDict

from .sandbox_perm_template_type import SandboxPermTemplateType


class SandboxPermBasicData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class HomeEntryDisplayData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        displayId: str
        topicId: str
        startTs: int
        endTs: int

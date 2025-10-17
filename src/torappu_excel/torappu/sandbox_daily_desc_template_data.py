from .sandbox_daily_desc_template_type import SandboxDailyDescTemplateType
from ..common import BaseStruct


class SandboxDailyDescTemplateData(BaseStruct):
    type: SandboxDailyDescTemplateType
    templateDesc: list[str]

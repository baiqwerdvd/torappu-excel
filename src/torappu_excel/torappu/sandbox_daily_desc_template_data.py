from .sandbox_daily_desc_template_type import SandboxDailyDescTemplateType
from ..common import BaseStruct

from msgspec import field


class SandboxDailyDescTemplateData(BaseStruct):
    type_: SandboxDailyDescTemplateType = field(name="type")
    templateDesc: list[str]

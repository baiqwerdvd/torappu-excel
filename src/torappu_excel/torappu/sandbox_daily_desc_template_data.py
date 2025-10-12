from pydantic import BaseModel, ConfigDict

from .sandbox_daily_desc_template_type import SandboxDailyDescTemplateType


class SandboxDailyDescTemplateData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: SandboxDailyDescTemplateType
    templateDesc: list[str]

from pydantic import BaseModel, ConfigDict

from .profession_category import ProfessionCategory


class SandboxV2LogisticsData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    desc: str
    noBuffDesc: str
    iconId: str
    profession: ProfessionCategory
    sortId: int
    levelParams: list[str]

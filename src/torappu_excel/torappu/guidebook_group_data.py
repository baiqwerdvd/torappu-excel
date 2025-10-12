from pydantic import BaseModel, ConfigDict

from .guidebook_config_data import GuidebookConfigData
from .uiguide_target import UIGuideTarget


class GuidebookGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    guideTarget: UIGuideTarget
    subSignal: str | None
    configList: list[GuidebookConfigData]

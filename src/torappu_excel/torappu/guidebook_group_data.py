from .guidebook_config_data import GuidebookConfigData
from .uiguide_target import UIGuideTarget
from ..common import BaseStruct


class GuidebookGroupData(BaseStruct):
    groupId: str
    guideTarget: UIGuideTarget
    subSignal: str | None
    configList: list[GuidebookConfigData]

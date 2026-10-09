from .ark_odc_task_tracking_entry_data import ArkOdcTaskTrackingEntryData
from ..common import BaseStruct


class ArkOdcTaskTrackingMainData(BaseStruct):
    questId: str
    priority: int
    title: str
    startBannerDesc: str
    completeBannerDesc: str
    entryDict: dict[str, ArkOdcTaskTrackingEntryData]

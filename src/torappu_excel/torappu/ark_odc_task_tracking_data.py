from .ark_odc_task_tracking_main_data import ArkOdcTaskTrackingMainData
from ..common import BaseStruct


class ArkOdcTaskTrackingData(BaseStruct):
    mainDataDict: dict[str, ArkOdcTaskTrackingMainData]

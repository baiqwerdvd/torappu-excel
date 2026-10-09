from .ark_odc_const_data import ArkOdcConstData
from .ark_odc_loading_data import ArkOdcLoadingData
from .ark_odc_move_const_data import ArkOdcMoveConstData
from .ark_odc_task_tracking_const_data import ArkOdcTaskTrackingConstData
from .ark_odc_task_tracking_data import ArkOdcTaskTrackingData
from .item_bundle import ItemBundle
from ..common import BaseStruct


class ArkOdcBasicData(BaseStruct):
    topicId: str
    rewardGroups: dict[str, list[ItemBundle]]
    moveConstData: ArkOdcMoveConstData
    loadingData: dict[str, ArkOdcLoadingData]
    constData: ArkOdcConstData
    taskTrackingConstData: ArkOdcTaskTrackingConstData
    clientTrackingData: ArkOdcTaskTrackingData

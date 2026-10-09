from .arkvent_camera_config_data import ArkventCameraConfigData
from .arkvent_task_actor_data import ArkventTaskActorData
from ..common import BaseStruct


class ArkventTaskData(BaseStruct):
    topicId: str
    actorData: dict[str, ArkventTaskActorData]
    varSeqData: list[str]
    cameraConfigData: dict[str, ArkventCameraConfigData]

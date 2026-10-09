from .vector3 import Vector3
from ..common import BaseStruct


class ArkventSceneData(BaseStruct):
    sceneId: str
    sceneIdHash: int
    sceneName: str
    assetId: str
    spawnPos: Vector3
    spawnRadius: float
    moveCameraConfigId: str
    idleCameraConfigId: str

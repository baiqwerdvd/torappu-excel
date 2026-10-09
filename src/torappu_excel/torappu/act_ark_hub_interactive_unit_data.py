from .act_ark_hub_actor_type import ActArkHubActorType
from .arkvent_range_data import ArkventRangeData
from .arkvent_spine_face_type import ArkventSpineFaceType
from .vector3 import Vector3
from ..common import BaseStruct


class ActArkHubInteractiveUnitData(BaseStruct):
    editorActorId: int
    actorInteractPointCount: int
    displayNameId: str
    unitId: str
    assetId: str
    actorType: ActArkHubActorType
    actorParam: str
    avgId: str | None
    interactionRequirements: list[str]
    position: Vector3
    yaw: float
    blockRange: ArkventRangeData
    interactRange: ArkventRangeData
    triggerCameraConfig: str
    interactCameraConfig: str
    interactBtnStyleId: str
    headUpStyleId: str
    sceneId: int
    overrideAnimConfig: dict[str, str] | None
    spineFace: ArkventSpineFaceType
    hasSafePos: bool
    safePos: Vector3

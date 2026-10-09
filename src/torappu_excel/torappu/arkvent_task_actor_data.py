from .arkvent_npc_spine_type import ArkventNPCSpineType
from .arkvent_range_data import ArkventRangeData
from .arkvent_spine_face_type import ArkventSpineFaceType
from .arkvent_task_actor_trigger_operation import ArkventTaskActorTriggerOperation
from .arkvent_task_actor_trigger_type import ArkventTaskActorTriggerType
from .arkvent_task_actor_type import ArkventTaskActorType
from .arkvent_task_show_condition import ArkventTaskShowCondition
from .vector3 import Vector3
from ..common import BaseStruct


class ArkventTaskActorData(BaseStruct):
    actorId: str
    actorNameId: str | None
    actorEnvLineId: str | None
    sceneId: int
    isGlobal: bool
    charId: str | None
    skinId: str | None
    arkventSpineId: str | None
    npcSpineType: ArkventNPCSpineType
    overrideAnimConfig: dict[str, str] | None
    furnitureAssetId: str | None
    actorType: ArkventTaskActorType
    actorPosition: Vector3
    actorYaw: float
    actorShowCondition: list[ArkventTaskShowCondition]
    actorTriggerType: ArkventTaskActorTriggerType
    actorTriggerOperations: dict[str, list[ArkventTaskActorTriggerOperation]] | None
    triggerRange: ArkventRangeData | None
    colliderRange: ArkventRangeData | None
    interactRange: ArkventRangeData | None
    triggerCameraConfig: str | None
    interactCameraConfig: str | None
    sceneStatusDriverId: str | None
    sceneObjectStatus: str | None
    effectId: str | None
    effectOffsetY: float
    interactBtnStyleId: str | None
    interactingBtnStyleId: str | None
    interactSoundFx: str | None
    headUpStyleId: str | None
    spineFace: ArkventSpineFaceType
    persistFaceWhenInteract: bool
    hasSafePos: bool
    safePos: Vector3

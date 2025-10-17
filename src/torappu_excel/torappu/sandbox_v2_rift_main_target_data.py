from .sandbox_v2_rift_main_target_type import SandboxV2RiftMainTargetType
from ..common import BaseStruct


class SandboxV2RiftMainTargetData(BaseStruct):
    id: str
    title: str
    desc: str
    storyDesc: str
    targetDayCount: int
    targetType: SandboxV2RiftMainTargetType
    questIconId: str | None
    questIconName: str | None

from .sandbox_v2_rift_main_target_type import SandboxV2RiftMainTargetType
from ..common import BaseStruct

from msgspec import field


class SandboxV2RiftMainTargetData(BaseStruct):
    id_: str = field(name="id")
    title: str
    desc: str
    storyDesc: str
    targetDayCount: int
    targetType: SandboxV2RiftMainTargetType
    questIconId: str | None
    questIconName: str | None

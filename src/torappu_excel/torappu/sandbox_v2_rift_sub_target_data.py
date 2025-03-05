from ..common import BaseStruct

from msgspec import field


class SandboxV2RiftSubTargetData(BaseStruct):
    id_: str = field(name="id")
    name: str
    desc: str

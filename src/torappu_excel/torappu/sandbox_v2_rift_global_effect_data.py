from ..common import BaseStruct

from msgspec import field


class SandboxV2RiftGlobalEffectData(BaseStruct):
    id_: str = field(name="id")
    desc: str

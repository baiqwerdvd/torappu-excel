from ..common import BaseStruct

from msgspec import field


class SandboxV2RiftParamData(BaseStruct):
    id_: str = field(name="id")
    desc: str
    iconId: str
    bkColor: str

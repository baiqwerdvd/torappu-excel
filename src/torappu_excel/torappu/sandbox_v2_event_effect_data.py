from ..common import BaseStruct


class SandboxV2EventEffectData(BaseStruct):
    eventEffectId: str
    buffId: str
    duration: int
    desc: str

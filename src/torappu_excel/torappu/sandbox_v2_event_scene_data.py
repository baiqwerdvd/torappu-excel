from ..common import BaseStruct


class SandboxV2EventSceneData(BaseStruct):
    eventSceneId: str
    title: str
    desc: str
    choiceIds: list[str]

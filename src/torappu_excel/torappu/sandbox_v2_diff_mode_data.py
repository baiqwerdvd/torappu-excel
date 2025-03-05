from ..common import BaseStruct


class SandboxV2DiffModeData(BaseStruct):
    title: str
    desc: str
    buffList: list[str]
    detailList: str
    sortId: int

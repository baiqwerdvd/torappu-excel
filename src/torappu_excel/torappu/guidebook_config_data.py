from ..common import BaseStruct


class GuidebookConfigData(BaseStruct):
    configId: str
    sortId: int
    pageIdList: list[str]

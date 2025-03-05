from ..common import BaseStruct


class SandboxBuildProduceData(BaseStruct):
    itemProduceId: str
    itemId: str
    itemTypeText: str
    materialItems: dict[str, int]

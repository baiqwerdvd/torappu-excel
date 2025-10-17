from ..common import BaseStruct


class SandboxFoodProduceData(BaseStruct):
    itemId: str
    mainMaterialItems: list[str]
    buffId: str
    unlockDesc: str

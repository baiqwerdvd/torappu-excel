from ..common import BaseStruct


class RoguelikeCopperModuleConsts(BaseStruct):
    copperDrawMaxNum: int
    copperDrawMinNum: int
    copperAllLuckyLevelGildId: str
    copperDrawFreezeCostItemId: str
    copperDrawFreezeCostCount: list[int]

from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActVecBreakDefenseStageData(BaseStruct):
    stageId: str
    sortId: int
    buffId: str
    defenseCharLimit: int
    bossIconId: str
    reward: ItemBundle

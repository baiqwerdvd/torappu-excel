from ..common import BaseStruct


class Act1VHalfIdleStageProductionData(BaseStruct):
    stageId: str
    fixedProduction: list[str]
    productionData: dict[str, "Act1VHalfIdleStageProductionData.ItemProductionData"]

    class ItemProductionData(BaseStruct):
        itemId: str
        efficiencyMax: int
        isFixed: bool
        maxDropValue: int

from pydantic import BaseModel, ConfigDict


class Act1VHalfIdleStageProductionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    fixedProduction: list[str]
    productionData: dict[str, "Act1VHalfIdleStageProductionData.ItemProductionData"]

    class ItemProductionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemId: str
        efficiencyMax: int
        isFixed: bool
        maxDropValue: int

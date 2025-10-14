from pydantic import BaseModel, ConfigDict


class PlayerBuildingWorkshopBuffBonus(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    formulaType: str
    apCond: int
    bonusNeed: int

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ActVecBreakDefenseStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    sortId: int
    buffId: str
    defenseCharLimit: int
    bossIconId: str
    reward: ItemBundle
